# Carousel image sources

Original image bytes are retained alongside the edited display derivatives. Crops are non-destructive SVG viewports in the templates; microscopy scale bars remain visible. Existing Korean post text and the slide 3 SVG are unchanged.

## Reuse status

The AMD Fiji photo is verified as CC BY-SA 4.0 on its Wikimedia Commons file page. The current display uses an AI-assisted background-removal derivative, with rotation; see the cutout revision below. Credit and the license URL are visible on slide 11. Preserve attribution and the license when sharing the photo; adaptations must follow its ShareAlike terms. This record does not apply a blanket license to the project or other images.

No explicit permission for public Instagram reuse was verified for the other six images. Their availability on a manufacturer or publisher site is not an open license. These are visual drafts, not a claim of publication clearance. Confirm appropriate reuse rights or replace those assets before public posting.

## Per-slide record

### Slide 1

Original NVIDIA page identifies this as the H100 GPU SXM5 module. Full 892px version advertised in srcset.

- Local file: `photos/h100-sxm5.jpg`
- Resolution: 892 × 415
- Credit: Image: NVIDIA
- Source: https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
- Image: https://developer-blogs.nvidia.com/wp-content/uploads/2022/03/SXM5-White-4-NEW-FINAL.jpg
- Reuse: No explicit public-reuse permission verified; draft use only pending rights review
- Display: Resized for display; no source content edited

### Slide 5

Philtech identifies this as its TSV interposer cross-sectional SEM; image shows vertical electrodes, not lateral routing.

- Local file: `photos/tsv-interposer.jpg`
- Resolution: 639 × 519
- Credit: Image: Philtech
- Source: https://www.philtech.co.jp/en/testwafer/assembly-wafer/
- Image: https://www.philtech.co.jp/cms/wp-content/uploads/2026/09/05_tsv-interposer-cross-section-sem.jpg
- Reuse: No explicit public-reuse permission verified; draft use only pending rights review
- Display: Resized for display; no source content edited

### Slide 8

Source Figure 4 identifies left panel (a) as TSV/bonding metrology; right panel (b) shows defects and is excluded.

- Local file: `photos/tsv-cross-sections.jpg`
- Resolution: 853 × 352
- Credit: Image: Thermo Fisher Scientific · Fig. 4(a)
- Source: https://www.thermofisher.com/blog/semiconductors/?p=444
- Image: https://www.thermofisher.com/blog/semiconductors/wp-content/uploads/sites/23/2023/06/advpack4.png
- Reuse: No explicit public-reuse permission verified; draft use only pending rights review
- Display: Panel selected using SVG viewport; scale bar retained

### Slide 9

Source PBGA page includes this six-layer construction diagram. It is an illustration, not a microscopy cross-section.

- Local file: `photos/pbga-substrate.png`
- Resolution: 339 × 205
- Credit: Image: Korea Circuit
- Source: https://koreacircuit-en.imweb.me/pbga
- Image: https://cdn.imweb.me/upload/S202605129fc2b87c9458e/33e7f4b296cb9.png
- Reuse: No explicit public-reuse permission verified; draft use only pending rights review
- Display: Resized for display; no source content edited

### Slide 10

Philtech identifies left panel as NiAu and right panel as SnAg; only right panel is displayed. This is not identified as a specific C4 implementation.

- Local file: `photos/bump-sem.jpg`
- Resolution: 1000 × 426
- Credit: Image: Philtech
- Source: https://www.philtech.co.jp/en/testwafer/assembly-wafer/
- Image: https://www.philtech.co.jp/cms/wp-content/uploads/2026/09/04_current-bump-sem.jpg
- Reuse: No explicit public-reuse permission verified; draft use only pending rights review
- Display: Panel selected using SVG viewport; scale bar retained

### Slide 11

Commons description identifies AMD Fiji GPU with HBM and interposer; used as a placement example, not as evidence of TSMC CoWoS-S.

- Local file: `photos/amd-fiji.jpg`
- Resolution: 3872 × 2592
- Credit: Photo: C. Spille / PC Games Hardware · CC BY-SA 4.0
- Source: https://commons.wikimedia.org/wiki/File:AMD_Fiji_GPU_package_with_GPU,_HBM_memory_and_interposer.jpg
- Image: https://upload.wikimedia.org/wikipedia/commons/e/e7/AMD_Fiji_GPU_package_with_GPU%2C_HBM_memory_and_interposer.jpg
- Reuse: CC BY-SA 4.0 verified on Wikimedia Commons file page
- Display: Displayed at reduced size, without cropping or annotations

### Slide 12

Source Figure 3 identifies a digital HBM cross-section extracted from Versa XRM 3D data. This is X-ray microscopy, not SEM.

- Local file: `photos/hbm-xrm.jpg`
- Resolution: 1024 × 374
- Credit: Image: ZEISS / 3D InCites · Fig. 3
- Source: https://www.3dincites.com/2020/04/digital-cross-section-technology-for-inspecting-and-meauring-buried-package-interconnects/
- Image: https://3dincites-imaps.nyc3.digitaloceanspaces.com/wp-content/uploads/20240828111950/HiddenFIguresFig3-1024x374.jpg
- Reuse: No explicit public-reuse permission verified; draft use only pending rights review
- Display: Panel selected using SVG viewport; scale bar retained

## Visual review

- Slide 9: the original is only 339 × 205 and is a diagram, not the requested microscopy photo. It is displayed at native dimensions. Replace it with a higher-resolution substrate micrograph if that photographic look is essential.
- Slide 10: the image stays short to preserve the dense original text at 34px; a larger photo would require an editorial change or a different slide format.
- Slide 11: original Korean source-detail reminder is retained. The AMD photo does not illustrate the specific CoWoS-S implementation mentioned in the text.

Full provenance, hashes, dimensions, crop coordinates, and review status are recorded in `sources.json`.

## Cutout revision

The NVIDIA and AMD package images now use transparent PNG derivatives made with AI-assisted background removal. These are editorial visual derivatives, not pixel-exact technical evidence; retain the original JPEGs for reference. The AMD derivative remains CC BY-SA 4.0, with C. Spille / PC Games Hardware attribution. Changes: background removal and display rotation. Microscopy originals are unchanged; only the display edges are softly masked, with the bottom scale-bar strip kept opaque. They are not fully isolated specimen cutouts.
