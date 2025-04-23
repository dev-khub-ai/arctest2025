Below is a generalized, self-contained prompt designed to help a chatbot solve similar grid transformation tasks (like those in ARC) that require detecting local object programs and stamping a transformed template onto an output grid. This prompt is written so as not to reference any specific task (such as Task 88) but instead provides general procedures and guidelines that you can apply whenever the problem exhibits the following characteristics:

- The input is a grid with various nonzero colored or numbered pixels.
- Certain groups of connected pixels (often specified by a particular value, e.g. “8”) form distinguishable objects.
- There is a need to detect additional “program–bar” pixels adjacent to these objects that determine transformation parameters.
- A template is extracted from the object’s bounding region, its pixels are modified according to the program–bar values, and this template is then stamped at positions in the grid determined by target selection.
- The final output is the union of all stamping operations, and the solution must be consistent whether a stamp is computed in isolation or as part of the complete grid.

Below is the prompt you can export and provide to another chatbot.

---

**Generalized Prompt for Solving Grid Transformation Tasks Involving Local Program Stamping**

You are a highly skilled assistant in solving grid-based visual and logical puzzles (such as those from the ARC dataset) that require a “local program stamping” transformation. In such tasks, you are given an input grid and must derive an output grid by performing the following steps:

### 1. Object Detection and Bounding Box Construction

- **Identify Objects:**  
  Scan the input grid for connected components that serve as the “core” of a transformation. These are usually groups of pixels with a specific value (for example, all cells with value 8) that form an “S–shape” or similar object.
  
- **Compute Bounding Boxes:**  
  For each detected object, compute its minimal bounding box (the smallest rectangle that covers all pixels of the object).

### 2. Program–Bar Identification

- **Examine the Border:**  
  Look at the cells immediately bordering each object’s bounding box (those that share an edge with the bounding box). Search for a pair of adjacent, nonzero cells that do not belong to the object’s original defining value.
  
- **Assign Values:**  
  Among the two adjacent candidates, designate:
  - The candidate with the smaller distance to the object as **c₁** (the “nearer” bar candidate).
  - The other candidate as **c₂** (the “farther” bar candidate).  
  (Distance can be measured using Manhattan or Euclidean metrics, with a chosen tiebreak rule if needed.)

### 3. Revised Anchor Selection

- **Define the Anchor:**  
  The anchor is the crucial pixel within the detected object (inside the bounding box) that determines where the transformation template will “hook” to the object.  
  - Ideally, the anchor should be a pixel in the object that is *strictly edge-adjacent* (sharing a side) to the candidate cell c₁ from the program–bar.
  - **If no pixel qualifies by strict edge-adjacency**, choose instead the object pixel that minimizes the Euclidean distance to c₁. Use a predetermined tiebreak rule (for example, selecting the top–leftmost among equally close candidates).  
  - Compute the **Anchor–Relative Offset** as follows:  
    \[
    \text{Offset} = (\text{Anchor Coordinate}) - (\text{Top–Left Coordinate of the Bounding Box})
    \]

### 4. Template Extraction

- **Extract the Template:**  
  From the object’s bounding box, extract a subgrid that serves as the stamping template.  
- **Modify the Template:**  
  Replace every pixel in the template that belongs to the object (for instance, every “8”) with the value c₁. Leave any background pixels (typically 0) unchanged.  
- The template should preserve the spatial arrangement of the object while “coloring” its pixels with c₁.

### 5. Target Selection

- **Scan the Input for Targets:**  
  Identify all cells in the input grid whose value equals c₂. These cells will be the targets where the template is to be stamped.
- **Global Exclusion Zone:**  
  Exclude any target cells that are within the global exclusion zone, which is defined as all cells inside any object’s bounding box plus those cells identified as part of any program–bar.  
- The remaining valid targets are where the stamp will be applied.

### 6. Stamping Procedure

- **Compute Stamp Position:**  
  For each valid target cell T, compute the stamp’s top–left coordinate using the formula:
  \[
  \text{Stamp Top–Left} = T - (\text{Anchor–Relative Offset})
  \]
  
- **Overlay the Template:**  
  Place (or “stamp”) the entire template onto an output grid (initially all zeros) at the computed position.
  - Only nonzero values in the template overwrite the output.
  - If any part of the template falls outside the grid boundaries, clip appropriately.

- **Deterministic Ordering:**  
  Apply the stamps in a deterministic order (for example, sorted by row and then by column) so that the effect of an isolated stamp is exactly replicated when all stamps are combined.

### 7. Combining Stamps and Final Output

- **Union of Stamps:**  
  The final output grid is the union of all individual stamp placements. When stamps overlap, define a rule (for example, later stamps overwrite earlier ones) that is consistent with the isolated stamp outcome.

### 8. Task Applicability Guidelines

This procedure is applicable to ARC tasks or similar grid–transformation puzzles where:
- The input grid contains connected components (objects) formed by pixels with a particular value.
- There exist adjacent “program–bar” cells that determine transformation parameters.
- A transformation template is to be extracted from the object and stamped at target locations based on matching a specific target color.
- The expected output shows that parts of the grid are generated by reusing a transformed version of an object from the input.

Use the above generalized steps to compute the output grid. Ensure that the anchor selection, template extraction, and deterministic application of stamps are done consistently so that the isolated stamp behavior matches the full-run output.

