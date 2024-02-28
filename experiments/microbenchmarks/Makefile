CC = gcc
CXX = g++
AS = as
LD = ld

CXX_FLAGS = -c -Wa,-adhln -g
ASFLAGS = -c
LDFLAGS =

SRC_DIR = src
BUILD_DIR = build

.PHONY: all clean $(BUILD_DIR)/runALU $(BUILD_DIR)/runMEMC $(BUILD_DIR)/runALUpcm

all: $(BUILD_DIR)/runALU $(BUILD_DIR)/runMEMC

$(BUILD_DIR)/runALUpcm: $(BUILD_DIR)/mainALUpcm.o $(BUILD_DIR)/workALU.o
	$(CXX) -L./intel-pcm-lite/build -o $@ $^ -lintelpcmlite

##g++ -I./intel-pcm-lite/include -L./intel-pcm-lite/build -o build/mainALUpcm.o src/mainALUpcm.cpp -lintelpcmlite
$(BUILD_DIR)/mainALUpcm.o: $(SRC_DIR)/mainALUpcm.cpp
	$(CXX) -c -o $@ $< -I./intel-pcm-lite/include

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
