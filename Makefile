# Execute the "targets" in this file with `make <target>` e.g., `make test`.
#
# You can also run multiple in sequence, e.g. `make clean lint test serve-coverage-report`

build:
	bash run.sh build

clean:
	bash run.sh clean

help:
	bash run.sh help

install:
	bash run.sh install

lint-ci:
	bash run.sh lint:ci

generate-project:
	bash run.sh generate-project

# publish-prod:
# 	bash run.sh publish:prod

# publish-test:
# 	bash run.sh publish:test

# release-prod:
# 	bash run.sh release:prod

# release-test:
# 	bash run.sh release:test

test:
	bash run.sh run-tests
