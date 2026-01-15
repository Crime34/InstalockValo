# 🎯 Valo Instalock

Un outil d'instalock ultra-rapide pour Valorant avec interface graphique moderne.

## 📋 Description

**Valo Instalock** est une application desktop qui permet de sélectionner et verrouiller instantanément votre agent Valorant préféré. Grâce à un système de coordonnées préconfigurées et une activation par raccourci clavier (F8), vous pouvez instalock votre agent en quelques millisecondes.

### ✨ Fonctionnalités

- 🚀 **Instalock ultra-rapide** : Sélection et verrouillage en moins d'une seconde
- ⌨️ **Raccourci clavier** : Activation simple avec la touche F8
- 🎨 **Interface moderne** : UI sombre et intuitive avec CustomTkinter
- ⚙️ **Configuration facile** : Enregistrement des positions par simple survol
- 📦 **Tous les agents** : Support de tous les agents Valorant (25+ agents)
- 🔧 **Personnalisable** : Ajout/suppression d'agents à la volée

## 🛠️ Installation

### Prérequis

- Python 3.8 ou supérieur
- Windows OS
- Valorant installé

### Étapes d'installation

1. **Cloner le projet**
   ```bash
   git clone https://github.com/Crime34/InstalockValo.git
   cd InstalockValo
   ```

2. **Créer un environnement virtuel** (recommandé)
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```
   
   Ou manuellement :
   ```bash
   pip install customtkinter pyautogui keyboard
   ```

## 🚀 Utilisation

### Lancement de l'application

```bash
python main.py
```

Ou double-cliquez sur `ValoInstalock.vbs` pour un lancement silencieux.

### Configuration initiale

1. **Définir la position du bouton LOCK**
   - Allez dans l'onglet **Config**
   - Cliquez sur **"Set Lock Button Position"** (bouton rouge)
   - Après le compte à rebours, survolez le bouton LOCK dans Valorant
   - La position sera enregistrée automatiquement

2. **Ajouter des agents** (optionnel)
   - Cliquez sur **"Add New Agent"**
   - Entrez le nom de l'agent
   - Survolez l'icône de l'agent dans l'écran de sélection
   - La position sera enregistrée

> **Note** : Le fichier `config.json` contient déjà les positions de tous les agents pour une résolution 1920x1080. Si vous utilisez une autre résolution, vous devrez reconfigurer les positions.

### Utilisation en jeu

1. Lancez l'application
2. Sélectionnez votre agent dans le menu déroulant (onglet **Run**)
3. Attendez d'être dans l'écran de sélection d'agent dans Valorant
4. Appuyez sur **F8** pour instalock instantanément

Le statut affichera :
- 🟢 **READY (F8)** : Prêt à instalock
- 🔵 **LOCKED [Agent]** : Agent verrouillé avec succès
- 🔴 **SETUP REQUIRED** : Configuration nécessaire
- 🔴 **LOCK POS MISSING** : Position du bouton LOCK non définie

## 📁 Structure du projet

```
valo/
├── main.py              # Application principale avec interface GUI
├── automator.py         # Logique d'automation (clics)
├── config_manager.py    # Gestion de la configuration
├── config.json          # Positions des agents et du bouton LOCK
├── ValoInstalock.vbs    # Lanceur silencieux
├── analyze_reyna.py     # Utilitaire d'analyse (développement)
├── auto_config.py       # Configuration automatique (développement)
├── check_screen.py      # Vérification d'écran (développement)
└── venv/                # Environnement virtuel Python
```

## ⚙️ Configuration

### Fichier config.json

Le fichier `config.json` stocke les coordonnées de chaque agent et du bouton LOCK :

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

### Résolutions supportées

Les coordonnées par défaut sont configurées pour **1920x1080**. Pour d'autres résolutions :
- Utilisez l'interface de configuration pour réenregistrer les positions
- Ou modifiez manuellement `config.json`

## 🔧 Dépendances

| Package | Version | Description |
|---------|---------|-------------|
| `customtkinter` | Latest | Interface graphique moderne |
| `pyautogui` | Latest | Automation des clics souris |
| `keyboard` | Latest | Gestion des raccourcis clavier |

## ⚠️ Avertissements

> [!WARNING]
> **Utilisation à vos risques et périls**
> 
> Cet outil utilise l'automation pour interagir avec Valorant. Bien qu'il n'injecte aucun code dans le jeu et se contente de simuler des clics souris, son utilisation pourrait potentiellement violer les conditions d'utilisation de Riot Games.

> [!CAUTION]
> **Politique anti-triche**
> 
> L'utilisation de scripts d'automation peut être considérée comme de la triche par Riot Games. Utilisez cet outil en connaissance de cause et à vos propres risques.

## 🐛 Dépannage

### L'instalock ne fonctionne pas
- Vérifiez que Valorant est en mode fenêtré ou plein écran sans bordure
- Assurez-vous que les coordonnées correspondent à votre résolution
- Reconfigurer la position du bouton LOCK

### L'agent sélectionné n'est pas le bon
- Vérifiez votre résolution d'écran
- Reconfigurez les positions des agents via l'interface

### F8 ne répond pas
- Relancez l'application en mode administrateur
- Vérifiez qu'aucune autre application n'utilise F8

## 📝 Licence

Ce projet est fourni "tel quel" à des fins éducatives uniquement.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer de nouvelles fonctionnalités
- Améliorer la documentation

## 📧 Contact

Pour toute question ou suggestion, ouvrez une issue sur le [dépôt GitHub](https://github.com/Crime34/InstalockValo/issues).

---

**Disclaimer** : Cet outil est un projet personnel à but éducatif. L'auteur n'est pas responsable de toute conséquence liée à son utilisation.
