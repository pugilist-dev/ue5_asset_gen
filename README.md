# Unreal Engine 5 asset generator using LLM
## Getting Started
This is just a inference repo using the model trained in the paper: [Shap-E: Generating Conditional 3D Implicit Functions](https://arxiv.org/abs/2305.02463).
Clone this repository

```commandline
git clone https://github.com/pugilist-dev/ue5_asset_gen.git
```
### commands
Enter the `ue5_asset_gen` directory. Use the Makefile to run the pipeline. This project uses poetry to handle the environment. Python version is 3.12 or above.
change into the cloned directory
```commandline
cd ue5_asset_gen
```
Install poetry for environment handling
```commandline
make install-poetry
```
Install the dependency
```commandline
make install
```
Update the CLIP repository
```commandline
make update-clip
```
Generate 3D objects
```commandline
make infer
```
To skip running individual steps and run all at once
```commandline
make all
```
### Project organization
```
├── Makefile                <- `make` aliases; `make install`, `make data`, etc.
├── README.md               <- You really should read this
├── pyproject.toml          <- Project configuration file with package metadata, 
│                              configurations, and dependencies.
├── data                    <- Directory for storing data
│ ├── interim                   <- Intermediate data that has been transformed
│ ├── processed                 <- The final, canonical data sets for modeling
│ └── raw                       <- The original, immutable data dump
└── src                         <- inference pipeline source code, including supportive modules
