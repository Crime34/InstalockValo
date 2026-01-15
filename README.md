# 🎯 Valo Instalock

An ultra-fast instalock tool for Valorant with a modern graphical interface.

[![GitHub](https://img.shields.io/badge/GitHub-Crime34%2FInstalockValo-blue?logo=github)](https://github.com/Crime34/InstalockValo)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)

> 🇫🇷 [Version française](README.fr.md)

## 📋 Description

**Valo Instalock** is a desktop application that allows you to instantly select and lock your favorite Valorant agent. With a system of pre-configured coordinates and keyboard shortcut activation (F8), you can instalock your agent in milliseconds.

### ✨ Features

- 🚀 **Ultra-fast instalock**: Selection and locking in less than a second
- ⌨️ **Keyboard shortcut**: Simple activation with the F8 key
- 🎨 **Modern interface**: Dark and intuitive UI with CustomTkinter
- ⚙️ **Easy configuration**: Record positions by simple hovering
- 📦 **All agents**: Support for all Valorant agents (25+ agents)
- 🔧 **Customizable**: Add/remove agents on the fly

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- Windows OS
- Valorant installed

### Installation Steps

1. **Clone the project**
   ```bash
   git clone https://github.com/Crime34/InstalockValo.git
   cd InstalockValo
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or manually:
   ```bash
   pip install customtkinter pyautogui keyboard
   ```

## 🚀 Usage

### Launching the Application

```bash
python main.py
```

Or double-click on `ValoInstalock.vbs` for silent launch.

### Initial Configuration

1. **Set the LOCK button position**
   - Go to the **Config** tab
   - Click on **"Set Lock Button Position"** (red button)
   - After the countdown, hover over the LOCK button in Valorant
   - The position will be automatically saved

2. **Add agents** (optional)
   - Click on **"Add New Agent"**
   - Enter the agent name
   - Hover over the agent icon in the selection screen
   - The position will be saved

> **Note**: The `config.json` file already contains positions for all agents at 1920x1080 resolution. If you use a different resolution, you'll need to reconfigure the positions.

### In-Game Usage

1. Launch the application
2. Select your agent from the dropdown menu (**Run** tab)
3. Wait until you're in the agent selection screen in Valorant
4. Press **F8** to instalock instantly

The status will display:
- 🟢 **READY (F8)**: Ready to instalock
- 🔵 **LOCKED [Agent]**: Agent successfully locked
- 🔴 **SETUP REQUIRED**: Configuration needed
- 🔴 **LOCK POS MISSING**: LOCK button position not defined

## 📁 Project Structure

```
valo/
├── main.py              # Main application with GUI
├── automator.py         # Automation logic (clicks)
├── config_manager.py    # Configuration management
├── config.json          # Agent and LOCK button positions
├── ValoInstalock.vbs    # Silent launcher
├── analyze_reyna.py     # Analysis utility (development)
├── auto_config.py       # Auto configuration (development)
├── check_screen.py      # Screen verification (development)
└── venv/                # Python virtual environment
```

## ⚙️ Configuration

### config.json File

The `config.json` file stores the coordinates of each agent and the LOCK button:

```json
{
    "agents": {
        "Reyna": {
            "x": 704,
            "y": 310
        },
        "Jett": {
            "x": 548,
            "y": 310
        }
    },
    "lock_btn": {
        "x": 960,
        "y": 885
    }
}
```

### Supported Resolutions

Default coordinates are configured for **1920x1080**. For other resolutions:
- Use the configuration interface to re-record positions
- Or manually edit `config.json`

## 🔧 Dependencies

| Package | Version | Description |
|---------|---------|-------------|
| `customtkinter` | Latest | Modern graphical interface |
| `pyautogui` | Latest | Mouse click automation |
| `keyboard` | Latest | Keyboard shortcut management |

## ⚠️ Warnings

> [!WARNING]
> **Use at your own risk**
> 
> This tool uses automation to interact with Valorant. Although it doesn't inject any code into the game and only simulates mouse clicks, its use could potentially violate Riot Games' terms of service.

> [!CAUTION]
> **Anti-cheat policy**
> 
> Using automation scripts may be considered cheating by Riot Games. Use this tool with full knowledge and at your own risk.

## 🐛 Troubleshooting

### Instalock doesn't work
- Check that Valorant is in windowed or borderless fullscreen mode
- Make sure coordinates match your resolution
- Reconfigure the LOCK button position

### Wrong agent selected
- Check your screen resolution
- Reconfigure agent positions via the interface

### F8 doesn't respond
- Restart the application as administrator
- Check that no other application is using F8

## 📝 License

This project is provided "as is" for educational purposes only.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Improve documentation

## 📧 Contact

For any questions or suggestions, open an issue on the [GitHub repository](https://github.com/Crime34/InstalockValo/issues).

---

**Disclaimer**: This tool is a personal project for educational purposes. The author is not responsible for any consequences related to its use.
