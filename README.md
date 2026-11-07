# FMCW Radar

mmWave FMCW Radar for Contactless Health Monitoring

## Setup
1. Install Python version 3.12
2. Install Git
3. Clone repository
4. Setup venv
```bash
python3 -m venv .venv
source .venv/bin/activate
```
5. Install requirements
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### To recieve live radar data
1. Install Infineon radar development kit (RDK) version 3.6.5; includes SDK version 3.6.4
2. Install requirements
```bash
$RADAR_SDK = "~/Infineon/Tools/Radar-Development-Kit/3.6.5/assets/software/radar_sdk"
python -m pip install "$RADAR_SDK/python_wheels/ifxradarsdk-3.6.4+4b4a6245-py3-none-win_amd64.whl"
python -c "from ifxradarsdk import get_version_full; print(get_version_full())"
```

## Run

```bash
python main.py --source {model,live}
```