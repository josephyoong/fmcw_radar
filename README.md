# FMCW Radar

mmWave FMCW Radar for Contactless Health Monitoring

## Usage

### Setup
1. Install Python version 3.12
2. Install Git
3. Clone repository
4. Setup venv
```bash
python3 -m venv .venv
.venv\Scripts\Activate.ps1.
```
5. Install requirements
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

#### To receive live radar data
1. Install Infineon radar development kit (RDK) version 3.6.5; includes SDK version 3.6.4
2. Install requirements
```pwsh
$RADAR_SDK = "~/Infineon/Tools/Radar-Development-Kit/3.6.5/assets/software/radar_sdk"
python -m pip install "$RADAR_SDK/python_wheels/ifxradarsdk-3.6.4+4b4a6245-py3-none-win_amd64.whl"
python -c "from ifxradarsdk import get_version_full; print(get_version_full())"
```

### Run

```
python src/main.py --source live --estimator estimator1 --plot
python main.py --source model2 --estimator estimator1 --snr-db -15 --frames 500 --fast --evaluate --plot
python -m evaluation.montecarlo --source model2 --estimator estimator1 --frames 500
```

```
python main.py
```

|switch         |options                |effect
|---------------|-----------------------|--------------------
|--source       |live, model1, model2   |source
|--estimator    |estimator1             |estimator
|--frames       |                       |number of frames
|--evaluate     |
|--plot
|--fast

--source model2 unlocks 

|switch         |options                |effect
|---------------|-----------------------|--------------------
|--snr-db       |                       |SNR

```
python -m evaluation.montecarlo
```
sweeps SNR

|switch         |options                |effect
|---------------|-----------------------|--------------------
|--source       |live, model1, model2   |source
|--estimator    |estimator1             |estimator
|--frames       |                       |number of frames per SNR test

## Sources

### Live

### Model 1 (M1): Stationary single-point reflector

### Model 2 (M2): Stationary single-point reflector with white Gaussian noise

## Estimators

### Estimator 1 (E1): Displacement-from-phase

## Evaluation

Monte Carlo simulation

## Simulation Experiments

### E1 on M1: Displacement-from-phase estimator on a stationary single-point reflector

```
python main.py --source model1 --estimator estimator1 --frames 500 --fast --evaluate --plot
```

### E1 on M2: Displacement-from-phase estimator on a stationary single-point reflector with white Gaussian noise

```
python -m evaluation.montecarlo --source model2 --estimator estimator1 --frames 1000
```