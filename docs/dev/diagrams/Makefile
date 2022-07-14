IMAGE_NAME := diagrams

run: cloud_main_connectivity_profile_state_controller.png cloud_main_connectivity_azure_network.png cloud_main_connectivity_egress_gateway.png

%.png: %.py build
	docker run -v $$(pwd)/:/tmp/ $(IMAGE_NAME) $<

build: Dockerfile
	docker build . -t $(IMAGE_NAME)