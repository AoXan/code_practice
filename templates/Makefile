# Generic Makefile for Kaggle competitions
# Usage examples:
#   make download COMP=titanic
#   make submit COMP=titanic SUB=submissions/sub_v1.csv MSG="baseline"
#   make comp-zip COMP=titanic

COMP ?= titanic

download:
	mkdir -p data
	kaggle competitions download -c $(COMP) -p data

submit:
	@test -n "$(SUB)" || (echo "SUB is required (path to submission CSV)"; exit 1)
	@test -n "$(MSG)" || (echo "MSG is required (submission message)"; exit 1)
	kaggle competitions submit -c $(COMP) -f $(SUB) -m "$(MSG)"

comp-zip:
	zip -r $(COMP)-code.zip notebooks src configs -x "*.ipynb_checkpoints*"
