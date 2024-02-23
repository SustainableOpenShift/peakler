CC = gcc
AS = as
LD = ld

ASFLAGS = -c
LDFLAGS =

SRC_DIR = src
BUILD_DIR = build

.PHONY: all clean $(BUILD_DIR)/runALU $(BUILD_DIR)/runMEMC

all: $(BUILD_DIR)/runALU $(BUILD_DIR)/runMEMC

$(BUILD_DIR)/runALU: $(BUILD_DIR)/mainALU.o $(BUILD_DIR)/workALU.o
	$(CC) -g $(LDFLAGS) $^ -o $@

$(BUILD_DIR)/mainALU.o: $(SRC_DIR)/mainALU.c
	$(CC) -c -g $< -o $@

$(BUILD_DIR)/workALU.o: $(SRC_DIR)/workALU.S
	$(CC) $(ASFLAGS) -DREPEAT_COUNT=$(COUNT) -Wa,-adhln -g $< -o $@

$(BUILD_DIR)/runMEMC: $(BUILD_DIR)/mainMEMC.o $(BUILD_DIR)/workMEMC.o
	$(CC) -g $(LDFLAGS) $^ -o $@

$(BUILD_DIR)/mainMEMC.o: $(SRC_DIR)/mainMEMC.c
	$(CC) -c -g $< -o $@

$(BUILD_DIR)/workMEMC.o: $(SRC_DIR)/workMEMC.S
	$(CC) $(ASFLAGS) -DREPEAT_COUNT=$(COUNT) -Wa,-adhln -g $< -o $@

clean:
	rm -f $(BUILD_DIR)/*.o $(BUILD_DIR)/runALU $(BUILD_DIR)/runMEMC
