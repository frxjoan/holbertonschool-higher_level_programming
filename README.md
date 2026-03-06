# Holberton School — Higher Level Programming

Ce dépôt regroupe mes projets du cursus **Higher Level Programming** chez Holberton.
Il contient principalement des exercices en Python, SQL et API, organisés par thèmes.

## Structure du dépôt

### Python Fundamentals
- `python-hello_world` — premières bases Python
- `python-if_else_loops_functions` — conditions, boucles, fonctions
- `python-import_modules` — imports, arguments CLI, modules
- `python-data_structures` — listes, tuples, chaînes, structures simples
- `python-more_data_structures` — sets, dictionnaires, lambda, map/filter/reduce

### Python OOP / Advanced Concepts
- `python-classes` — classes et objets
- `python-more_classes` — approfondissement OOP
- `python-inheritance` — héritage et polymorphisme
- `python-input_output` — fichiers et sérialisation simple
- `python-exceptions` — gestion d’exceptions
- `python-test_driven_development` — doc-tests et tests unitaires
- `python-abc` — classes abstraites, duck typing, itérateurs
- `python-serialization` — sérialisation Python
- `python-object_relational_mapping` — SQLAlchemy et ORM

### SQL
- `SQL_introduction` — requêtes SQL de base
- `SQL_more_queries` — jointures, sous-requêtes, permissions

### API
- `restful-api` — exercices autour des API REST

## Fichiers à la racine
- `main.py` — script de test/entrée rapide
- `test.py` — script de test local

## Prérequis
- Python 3.8+
- `pycodestyle` (selon les projets)
- MySQL / SQLAlchemy pour la partie ORM

## Exécution rapide

Se placer dans un dossier projet puis exécuter un fichier :

```bash
cd python-hello_world
python3 2-print.py
```

Exemple avec tests (si présents) :

```bash
python3 -m doctest -v ./tests/*
python3 -m unittest discover
```

## Objectif pédagogique

Ce dépôt suit une progression pratique :
1. maîtriser les bases Python,
2. construire une bonne rigueur de code,
3. appliquer l’OOP, les tests et la persistance,
4. relier Python aux bases de données et aux API.
