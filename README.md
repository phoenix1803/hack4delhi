# hack4delhi

This repository contains geospatial data, rainfall analysis notebooks, and model artifacts used to study urban flooding and infrastructure risk in Delhi. It combines map visualization, historical rainfall analysis, and model-driven prioritization for drains and roads.

## What this project contains

The project has three major parts:

1. A browser map viewer that overlays drains, roads, and waterlogging zones.
2. Data science notebooks and datasets for rainfall and risk modeling.
3. Trained model artifacts and derived CSV outputs for prioritization and impact assessment.

## Repository structure in detail

### Root files

`index.html`
Main Leaflet-based map interface. It loads and visualizes:

- `drains_data.json`
- `roads_data.json`
- `waterlogging_data.json`

The UI includes layer toggles, a legend, and feature count stats.

`serve_map.py`
Simple local HTTP server launcher for map testing. It starts a server on port 8000 and opens a browser automatically.

Important note: the script currently opens `infrastructure_map.html`, but the map file in this repository is `index.html`.

`drains_data.json`
Processed drain layer data used directly by the map.

`roads_data.json`
Processed road layer data used directly by the map.

`waterlogging_data.json`
Processed waterlogging zone data used directly by the map.

`.gitattributes`
Git LFS tracking rules for large data-centric file types (`.csv`, `.geojson`, `.nc`, `.ipynb`, `.json`).

### 7-days-rainfall-prediction/

Purpose: short-horizon rainfall forecasting experiments and outputs.

Files:

- `rainfall_prediction_ensemble.ipynb`: Notebook for building and/or evaluating an ensemble rainfall prediction workflow.
- `rainfall_forecast_7days.csv`: Forecast output for the next 7 days.
- `testset.csv`: Evaluation or holdout data used by the forecasting workflow.
- `rainfall_ensemble_model.pkl`: Serialized ensemble model artifact.

### gridded-rainfall-india/

Purpose: grid-based rainfall data exploration.

Files:

- `gridded_rainfall.nc`: NetCDF gridded rainfall dataset.
- `grid.ipynb`: Notebook for reading, analyzing, and visualizing gridded rainfall.

### historic-rainfall-data/

Purpose: archived rainfall records used for historical analysis and feature generation.

Files:

- `74fd035c-e32b-447f-a99c-91ecdfd8aa71.csv`
- `7b06b00c-befa-49d0-be1c-1fe9d5fdf26e.csv`

These CSV files appear to be source historical rainfall datasets consumed by notebooks or modeling scripts.

### models/

Purpose: model training/evaluation workspace and generated model outputs for risk ranking.

Files:

- `main.ipynb`: Central notebook for model experimentation or pipeline assembly.
- `drain_priority_rankings.csv`: Ranked drain segments by priority.
- `road_impact_assessment.csv`: Modeled impact analysis for road infrastructure.
- `elevation.tif`: Elevation raster likely used as a terrain/hydrology feature.
- `drain_priority_weights.pkl`: Serialized model/weights for drain prioritization.
- `impact_assessment_weights.pkl`: Serialized model/weights for impact assessment.
- `waterlogging_predictor_weights.pkl`: Serialized model/weights for waterlogging prediction.

### road/

Purpose: raw or staged road geospatial layers.

Files:

- `export (4).geojson`
- `export (5).geojson`
- `export (6).geojson`
- `export (7).geojson`

These are likely alternate exports, tiles, or batches of road geometry before consolidation.

### water-drains/

Purpose: raw or staged drain geospatial layers.

Files:

- `export.geojson`
- `export (1).geojson`
- `export (2).geojson`
- `export (3).geojson`

These appear to be multiple versions/chunks of drain network geometry.

### water-logging-with-cordds/

Purpose: clustering and severity modeling for waterlogging events, plus model artifacts for downstream use.

Top-level files:

- `cluster_risk_zones.ipynb`: Notebook for clustering flood/waterlogging risk zones.
- `drain_severity_prediction.ipynb`: Notebook for predicting severity at drain-related locations.
- `waterlogging_final.csv`: Curated/processed waterlogging dataset used in modeling.

Subfolders:

`public/data/waterlogging_model/`

- `best_model.pkl`: Primary trained model.
- `kmeans.pkl`: K-means clustering model.
- `cluster_dispersion.pkl`: Cluster spread statistics or calibration artifact.
- `scaler.pkl`: Feature scaling transformer.
- `severity_labels.pkl`: Mapping/labels for model output interpretation.

## Typical workflow across folders

1. Collect geospatial raw data from `road/` and `water-drains/`.
2. Process/export map-ready layers into root JSON files (`drains_data.json`, `roads_data.json`, `waterlogging_data.json`).
3. Analyze rainfall data via `historic-rainfall-data/`, `gridded-rainfall-india/`, and `7-days-rainfall-prediction/`.
4. Train or update models in `models/` and `water-logging-with-cordds/`.
5. Generate ranked outputs like `drain_priority_rankings.csv` and `road_impact_assessment.csv`.
6. Visualize results in `index.html`.

## Running the map locally

Option 1 (recommended):

1. From repository root, run a static server (for example with Python):

```bash
python -m http.server 8000
```

2. Open `http://localhost:8000/index.html`

Option 2:

Use `serve_map.py`, but update the target page from `infrastructure_map.html` to `index.html` first.

## Notes on large files and Git LFS

This repository tracks heavy data file types with Git LFS to keep Git history manageable and avoid oversized regular Git objects. If you clone this repository, ensure Git LFS is installed and initialized:

```bash
git lfs install
git lfs pull
```