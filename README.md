# bubble_sheet_grader
Simple python script to grade score matrix produced by OpenMCR. Allows weighting, multiple correct answers, negative scoring, etc.

Steps:
1. Install OpenMCR by following instructions on their GitHub page
2. Scan the bubble sheets using a scanner (or phone). One image per bubblesheet. Save all images to a single folder.
3. Launch OpenMCR.
    1. Set as Input Folder the folder containing all the images.
    2. Set as Output Folder the folder where you want the output csv to be saved.
    3. All other options set to default, especially make sure not to "convert mutiple answers to 'F'" or "empty answes to 'G'".
    4. Click Continue. Status update can be seen at the bottom of the dialog box.
    5. If successful, it shold read at the very bottom: "All exams processed and saved. No exam keys were found, so no scoring was performed".
    6. Press Close.
4. Prepare an answer-key.csv with 3 columns: question number, correct answers separated by a |, and weight.
   For example:
   ```
   Q1  B|D    2
   Q2  B      2
   Q3  A|B|D  4
   ```
   
6. Next, run this python script as follows:
   ```
   python openMCR-multi-answer.py <open_mcr_output_csv> answer-key.csv <output_filename>
   ```
