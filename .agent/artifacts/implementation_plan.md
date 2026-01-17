# Visual Enhancement Implementation Plan

## Goal

Elevate the visual presentation of "NeetCode 150 完全攻略" from a standard text-based documentation to a premium, visually engaging learning platform using Gemini 3 Pro generated assets.

## User Review Required

> [!NOTE]
> Due to current high demand on the Image Generation Model (`MODEL_CAPACITY_EXHAUSTED`), I have prepared the **Visual Architecture** and **Prompts** below. We can execute the generation steps as soon as capacity returns.

## Proposed Changes

### 1. Asset Directory Structure

Create a dedicated folder for high-resolution assets:
`docs/assets/images/`

- `logo.png` (Project Icon)
- `banners/` (Chapter Headers)

### 2. Visual Assets & Prompts

We will generate the following assets using these specific prompts:

#### A. Project Logo

> **Prompt**: "A minimalist, modern, tech logo for a coding project named 'NeetCode 150'. The design should combine a code bracket '{ }' and a stylized brain or neural network node to represent learning algorithms. Use a gradient color scheme with cyan, neon purple, and deep blue on a dark background. High resolution, vector art style, clean lines, suitable for a favicon or circular icon."

- **Usage**: Replace standard favicon in `mkdocs.yml` and add to README.

#### B. Chapter Hero Images (Banners)

Targeting the most popular/current chapters first:

| Chapter          | Prompt Concept                                                                                                                                                                                                                                                                                                                                                                                           |
| :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Two Pointers** | "Abstract 3D digital art representing the 'Two Pointers' algorithm. Two glowing beams of light or data streams traveling from opposite ends of a long horizontal futuristic highway towards a meeting point in the center. Cyberpunk aesthetic, neon blue and orange colors. deeply detailed, cinematic lighting, 8k resolution, wide aspect ratio."                                                     |
| **Stack**        | "Digital art representing a 'Stack' data structure (Last-In, First-Out). A vertical pillar of glowing, futuristic glass data blocks being stacked one on top of another. The top block is highlighting, emitting a brighter light, ready to be popped. Sci-fi laboratory setting with dark reflections. Vertical composition but framed for a wide header. 8k resolution, unreal engine 5 render style." |

### 3. Integration Strategy

#### `mkdocs.yml`

```yaml
theme:
  logo: assets/images/logo.png
  favicon: assets/images/logo.png
```

#### Chapter Index Pages (`docs/02_Two_Pointers/index.md`)

Add the banner at the top of the chapter index (or first file if index doesn't exist).

```markdown
![Two Pointers Hero](../assets/images/banners/two_pointers.png)

# Two Pointers

...
```

## Verification Plan

1.  **Generate Images**: Retry generation until successful.
2.  **Verify Rendering**: Run `mkdocs serve` to ensure images load correctly and look good in Light/Dark modes.
3.  **Responsiveness**: Check mobile view to ensure banners scale properly.
