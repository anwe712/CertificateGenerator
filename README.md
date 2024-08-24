# Certificate Generator

This is a simple project to generate certificates based on a dataset in CSV format. The certificates are created using a background image, and the data is overlaid on this image using Python libraries.

## Requirements

1. **Dataset**: A CSV file (`RaceResults.csv`) containing the following columns:
   - `Finish Position`
   - `BIB`
   - `NAME`
   - `NATIONALITY`
   - `Net Finish Time`

2. **Background Image**: An image (`bg.jpeg`) that will serve as the template for the certificates.

## Installation

To run this project, you need to have Python installed. Then, install the required packages using pip:

```bash
pip install pandas pillow
