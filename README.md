# Claude Code Web - Repository de Test

Bienvenue dans ce repository de test pour [Claude Code Web](https://claude.com/claude-code) !

## À propos

Ce repository sert à explorer et tester les capacités de Claude Code, l'assistant IA d'Anthropic pour le développement logiciel.

## Fonctionnalités à tester

Voici quelques exemples de ce que vous pouvez demander à Claude Code :

### Développement
- Créer des applications (web, CLI, scripts)
- Écrire et refactoriser du code
- Déboguer et corriger des erreurs
- Ajouter des tests unitaires

### Manipulation de fichiers
- Rechercher dans le code
- Lire et éditer des fichiers
- Organiser la structure du projet

### Git & GitHub
- Créer des commits
- Gérer des branches
- Créer des pull requests

### Analyse
- Expliquer du code existant
- Proposer des améliorations
- Analyser la structure d'un projet

## Exemples de commandes

```bash
# Créer une application simple
"Crée une application calculatrice en Python"

# Analyser le code
"Explique-moi comment fonctionne ce fichier"

# Git workflow
"Commit mes changements avec un message descriptif"
```

## Projets d'exemple

### 1. Calculatrice Web (HTML/CSS/JS)

Une calculatrice web moderne et interactive accessible directement dans le navigateur.

**Démo en ligne** : Activez GitHub Pages pour voir la démo !

#### Comment activer GitHub Pages :

1. Allez dans les **Settings** de votre repository GitHub
2. Dans le menu de gauche, cliquez sur **Pages**
3. Sous **Source**, sélectionnez la branche `claude/test-code-web-011CUTjiHkQcG2MW29FavDA3`
4. Cliquez sur **Save**
5. Attendez quelques minutes, votre site sera accessible à l'URL affichée

#### Fonctionnalités :

- Interface moderne avec dégradé de couleurs
- Opérations : addition, soustraction, multiplication, division
- Responsive design
- Support du clavier (chiffres, opérateurs, Enter, Escape, Backspace)
- Gestion des erreurs (division par zéro)

#### Utilisation locale :

Ouvrez simplement `index.html` dans votre navigateur !

---

### 2. Calculatrice CLI (Python)

Une calculatrice en ligne de commande avec tests unitaires.

#### Utilisation

Lancer la calculatrice :
```bash
python calculatrice.py
```

Exécuter les tests :
```bash
python test_calculatrice.py -v
```

#### Fonctionnalités

- Addition, soustraction, multiplication, division
- Gestion des erreurs (division par zéro)
- Tests unitaires complets (100% coverage)
- Interface en ligne de commande intuitive

## Structure du projet

```
claude-cc-test/
├── README.md
├── index.html               # Calculatrice Web
├── calculatrice.py          # Calculatrice CLI
├── test_calculatrice.py     # Tests unitaires
└── .gitignore               # Configuration Git
```

## Ressources

- [Documentation Claude Code](https://docs.claude.com/en/docs/claude-code)
- [Anthropic](https://anthropic.com)

---

Créé avec Claude Code
