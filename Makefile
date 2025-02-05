#################################################################################
# GLOBALS                                                                       #
#################################################################################
PYTHON	=	python3.12
PROJECT_DIR	=	$(CURDIR)
#################################################################################
# COMMANDS                                                                      #
#################################################################################
# Makefile
POETRY_INSTALL_URL=https://install.python-poetry.org

# Install poetry
.PHONY:	install-poetry
install-poetry:
	curl	-sSL	$(POETRY_INSTALL_URL)	|	$(PYTHON)	-

# Install dependencies
.PHONY:	install
install:	install-poetry
	poetry	install
	@echo	"Cloning shap-e repository..."
	git	clone	https://github.com/openai/shap-e.git
	cd shap-e &&	poetry	run	pip	install	setuptools	wheel &&	poetry	run	python	setup.py	install

.PHONY:	update-clip
update-clip:
	poetry	run	pip	uninstall	clip
	poetry	run	pip	install	git+https://github.com/openai/CLIP.git

# Remove shap-e
.PHONY:	remove-shap-e
remove-shap-e:
	rm	-rf	shap-e

# Update dependencies
.PHONY:	update
update:
	poetry	update

# Run inference
.PHONY:	run
run:
	poetry	run	python	-m	src.infer

.PHONY:	view
view:
	poetry	run	python	-m	src.view