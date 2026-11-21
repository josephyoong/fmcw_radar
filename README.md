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

### Model 3 (M3): Oscillating single-point reflector

### Model 4 (M4): Oscillating single-point reflector with white Gaussian noise

### Model 5 (M5): Oscillating single-point reflector with white Gaussian noise and single-point stationary clutter

Stationary clutter may return signals with high energy such that bin selection via highest mean energy over a frame is not suitable.

## Estimators

### Estimator 1 (E1): Displacement-from-phase

### Estimator 2 (E2):

### Estimator 3 (E3): Displacement-from-phase, bin selected by highest squared deviation

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

### E1 on M3: Displacement-from-phase estimator on an oscillating single-point reflector
```
python main.py --source model3 --estimator estimator1 --frames 200 --fast --evaluate --plot
```

### E1 on M4: Displacement-from-phase estimator on an oscillating single-point reflector with white Gaussian noise
```
python -m evaluation.montecarlo --source model4 --estimator estimator1 --frames 1000
```

### E2 on M3:
```
python main.py --source model3 --estimator estimator2 --frames 200 --fast --plot
```

### E2 on M4:
```
python main.py --source model4 --estimator estimator2 --frames 200 --fast --plot --snr-db 10
```

### E2 on M5:
```
python main.py --source model5 --estimator estimator2 --frames 200 --fast --plot --snr-db 10
```
Tracks the wrong reflector, so displacement estimate is wrong. Proves that bin selection method is bad.

### E3 on M5: 

New bin selection method, using 
```
python main.py --source model5 --estimator estimator3 --frames 200 --fast --plot --snr-db 10
```

### recording
```
python record.py --note "static clutter"
```
```
python main.py --source recording --recording --estimator estimator2 --fast --plot
```