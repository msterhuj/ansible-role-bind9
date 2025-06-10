IMAGES = \
  geerlingguy/docker-ubuntu2204-ansible \
  geerlingguy/docker-ubuntu2404-ansible \
  geerlingguy/docker-debian12-ansible \
  geerlingguy/docker-debian11-ansible

test-all:
	@for image in $(IMAGES); do \
	  echo "Testing $$image..."; \
	  IMAGE=$$image tox -e molecule || exit 1; \
	done