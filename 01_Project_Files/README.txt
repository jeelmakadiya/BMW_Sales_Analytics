# BMW Sales Performance Analytics

This beginner-friendly project includes an interactive Python dashboard, a PowerPoint presentation, a chart preview, and the source CSV.

## Files
- `app.py` — interactive Streamlit dashboard
- `BMW sales data (2010-2024).csv` — dataset used by the dashboard
- `BMW_Sales_Performance_Analysis.pptx` — presentation
- `dashboard_preview.png` — static preview chart
- `requirements.txt` — required Python packages

## Run the dashboard (Windows)
1. Install Python 3.10 or newer from python.org. During installation, tick **Add Python to PATH**.
2. Extract the ZIP file.
3. Open the extracted folder.
4. Click the folder address bar, type `cmd`, and press Enter.
5. Run:
   ```bash
   python -m pip install -r requirements.txt
   ```
6. Then run:
   ```bash
   python -m streamlit run app.py
   ```
7. The dashboard will open in your browser. Use the filters on the left to explore the data.

## Dataset notes
The CSV contains 50,000 rows and 11 columns: Model, Year, Region, Color, Fuel_Type, Transmission, Engine_Size_L, Mileage_KM, Price_USD, Sales_Volume, and Sales_Classification.

## Important interpretation note
The dashboard reports descriptive summaries of the supplied dataset. It does not establish real-world BMW sales totals unless the dataset itself is verified as official.
