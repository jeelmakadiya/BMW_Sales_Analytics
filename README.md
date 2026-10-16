# BMW Sales Analytics Dashboard

An interactive analytics project exploring **50,000 BMW sales records (2010–2024)** across 11 dimensions — model, region, year, fuel type, transmission, engine size, mileage, price, and sales volume.

Charts are built with [Plotly](https://plotly.com/javascript/). The main dashboard is delivered as a **single self-contained HTML file** — no server, no build step, no installation required.

![BMW Sales Performance Dashboard](03_Screenshots_and_Dashboard_Interaction_Video/screen%20short/1.png)

![Sales by fuel type, model performance, and price vs volume](03_Screenshots_and_Dashboard_Interaction_Video/screen%20short/2.png)

---

## Repository contents

| Folder | Contents |
|---|---|
| `01_Project_Files/` | `BMW_Sales_Interactive_Dashboard.html` (self-contained dashboard), `app.py` (Streamlit version), `requirements.txt`, `README.txt` |
| `02_Dataset_Files/` | `Processed_Dataset/` cleaned CSV, `Raw_Dataset/dataset.xlsx` original workbook |
| `03_Screenshots_and_Dashboard_Interaction_Video/` | three screenshots and a `video.mp4` walkthrough of the dashboard in use |
| `04_Report_Presentation_and_Dashboard_Screenshots/` | written `report.pdf`, `BMW_Sales_Performance_Analysis.pptx`, and a screenshot PDF |

---

## View the dashboard

### Option 1 — Static HTML (no setup)

Open `01_Project_Files/BMW_Sales_Interactive_Dashboard.html` in any modern browser.

The dataset is embedded in the file, so filters, charts, and the "Download Filtered CSV" button all work offline. Only the Plotly charting library is loaded from a CDN, so an internet connection is needed to render the charts.

### Option 2 — Streamlit app

Requires Python 3.10 or newer.

```bash
cd 01_Project_Files
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

The dashboard then opens in your browser with a filter sidebar.

---

## Dashboard features

- **Filter panel** — Year, Region, Model, Fuel Type, and Sales Classification
- **KPI cards** — total sales volume, total records, average price (USD), average mileage (km), average engine size (L)
- **Sales performance** — yearly sales trend and sales by region
- **Breakdowns** — sales by fuel type, top models by sales volume, average price by model
- **Relationships** — price vs. sales volume scatter, coloured by fuel type
- **Filtered data preview** and one-click **export of the filtered dataset to CSV**

---

## Dataset

`50,000 rows × 11 columns`:

`Model`, `Year`, `Region`, `Color`, `Fuel_Type`, `Transmission`, `Engine_Size_L`, `Mileage_KM`, `Price_USD`, `Sales_Volume`, `Sales_Classification`.

---

## Deployment

**Live dashboard:** https://bmw-sales-analytics.vercel.app

The static dashboard is hosted on **Vercel**. `vercel.json` rewrites the root URL to the dashboard file, so the site is reachable at `/` instead of the full file path.

To redeploy after a change:

```bash
vercel --prod
```

---

## Important interpretation note

This project reports **descriptive summaries of the supplied dataset only**. The figures shown should not be treated as verified, official BMW sales statistics unless the underlying dataset itself is confirmed as official.

---

## Author

**Jeel Makadiya** — [@jeelmakadiya](https://github.com/jeelmakadiya)
