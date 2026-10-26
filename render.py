# render.py
import json, sys, pathlib, shutil
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from jinja2 import Environment, FileSystemLoader, select_autoescape
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent
W, H = 1080, 1350


def render_post(json_path: pathlib.Path, page, env):
    post = json.loads(json_path.read_text(encoding="utf-8"))
    out = ROOT / "out" / post["slug"]
    out.mkdir(parents=True, exist_ok=True)
    total = len(post["slides"])
    for font in ("Pretendard-Regular.otf", "Pretendard-Bold.otf"):
        if not (ROOT / "fonts" / font).is_file():
            print(f"WARNING: missing {font}; falling back to system fonts")

    for slide in post["slides"]:
        slide = dict(slide)
        i = slide["index"]
        if slide.get("image") and not (ROOT / "assets" / slide["image"]["file"]).is_file():
            print(f"WARNING: slide {i}: missing image {slide['image']['file']}; skipped")
            slide.pop("image")
        ctx = {
            "slide": slide,
            "theme": post["theme"],
            "series": post["series"],
            "post_number": post["post_number"],
            "index": i,
            "total": total,
            "assets_uri": "../../assets",
            "fonts_uri": "../../fonts",
        }
        if slide["layout"] == "diagram":
            ctx["svg"] = (ROOT / "assets" / slide["diagram"]).read_text(encoding="utf-8")

        html = env.get_template(f"{slide['layout']}.html").render(**ctx)
        html_path = out / f"{i:02d}.html"
        html_path.write_text(html, encoding="utf-8")

        page.goto(env.globals["root_uri"] + "/" + html_path.relative_to(ROOT).as_posix(), wait_until="load")
        page.evaluate("document.fonts.ready.then(() => true)")
        page.evaluate("""() => {
            const title = document.querySelector('.cover-title');
            if (title) {
                while (title.getBoundingClientRect().height / parseFloat(getComputedStyle(title).lineHeight) >= 2.9 && parseFloat(getComputedStyle(title).fontSize) > 84) {
                    title.style.fontSize = (parseFloat(getComputedStyle(title).fontSize) - 2) + 'px';
                }
            }
            const body = document.querySelector('main');
            const fits = () => body.scrollHeight <= body.clientHeight + 1;
            const text = body.querySelector('.body-text');
            if (text && !fits()) text.classList.add('compact');
            if (text && !fits()) text.classList.add('compact-small');
            if (!fits()) throw new Error('Slide content overflows: ' + body.scrollHeight + ' > ' + body.clientHeight);
            for (const box of document.querySelectorAll('foreignObject')) {
                const content = box.firstElementChild;
                const bounds = box.getBoundingClientRect();
                if (content && (content.scrollHeight > bounds.height + 1 || content.scrollWidth > bounds.width + 1)) {
                    throw new Error('Diagram text is clipped: ' + content.textContent.trim());
                }
            }
        }""")
        page.screenshot(path=str(out / f"{i:02d}.png"),
                        clip={"x": 0, "y": 0, "width": W, "height": H})
        print(f"[{post['slug']}] slide {i:02d} -> {out / f'{i:02d}.png'}")


def main():
    paths = [pathlib.Path(p) for p in sys.argv[1:]] or sorted((ROOT / "posts").glob("*.json"))
    env = Environment(loader=FileSystemLoader(ROOT / "templates"),
                      autoescape=select_autoescape(["html"]))

    class QuietHandler(SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT)))
    Thread(target=server.serve_forever, daemon=True).start()
    env.globals["root_uri"] = f"http://127.0.0.1:{server.server_port}"
    with sync_playwright() as p:
        browser_path = pathlib.Path(p.chromium.executable_path)
        browser = p.chromium.launch(executable_path=None if browser_path.is_file() else shutil.which("chromium"))
        page = browser.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        for path in paths:
            render_post(path, page, env)
        browser.close()
    server.shutdown()
    server.server_close()


if __name__ == "__main__":
    main()