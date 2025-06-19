
SCENARIOS := default zone-transfer
IMAGES = \
  geerlingguy/docker-ubuntu2204-ansible \
  geerlingguy/docker-ubuntu2404-ansible \
  geerlingguy/docker-debian12-ansible \
  geerlingguy/docker-debian11-ansible

.PHONY: lint test-all

lint:
	@tox -e lint

test-all:
	@for scenario in $(SCENARIOS); do \
		for image in $(IMAGES); do \
			echo "=== Running Molecule scenario '$$scenario' with image '$$image' ==="; \
			IMAGE=$$image tox -e molecule -- --scenario-name $$scenario || exit 1; \
		done \
	done