# Keras Tuner

Utilize intelligent hyperparameters hyperband, baisian optimization, etc.

Compared to scikit-learn hyperparamters
logistic regression, svm, random forest, or wrap TF model in wrapper to tune nodes
dropout, learning, epochs, etc.
1. grid search
1. randomized search

Recommend GPU

Project layout

```angular2html
.
├── README.md
├── main.ipynb
├── main.py
├── output # populated with experiment output from train.py
│   ├── bayesian_plot.png
│   ├── hyperband_plot.png
│   ├── random
│   │   ├── oracle.json
│   │   ├── trial_8ccc6839061004c1f46f6744f3eb2884
│   │   │   ├── checkpoints
│   │   │   │   └── epoch_0
│   │   │   └── trial.json
│   │   ├── trial_d7f4ea6f3e07d08d7b8fefe1349d54d9
│   │   │   ├── checkpoints
│   │   │   │   └── epoch_0
│   │   │   │       ├── checkpoint
│   │   │   │       ├── checkpoint.data-00000-of-00001
│   │   │   │       └── checkpoint.index
│   │   │   └── trial.json
│   │   └── tuner0.json
│   └── random_plot.png
├── requirements.txt
├── submodules
│   ├── __init__.py
│   ├── config.py # stores configs
│   ├── model.py # deep NN implementation with hyperparam
│   └── utils.py
└── train.py # load a dataset, create an instance, tune hyperparameters

```