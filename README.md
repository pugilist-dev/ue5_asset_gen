# Unreal Engine 5 asset generator using LLM
## Getting Started
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
### Project organization
