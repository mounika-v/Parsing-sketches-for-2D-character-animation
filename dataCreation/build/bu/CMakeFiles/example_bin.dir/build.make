# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/mounika/MTP/sem

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/mounika/MTP/sem/build

# Include any dependencies generated for this target.
include CMakeFiles/example_bin.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/example_bin.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/example_bin.dir/flags.make

CMakeFiles/example_bin.dir/main.cpp.o: CMakeFiles/example_bin.dir/flags.make
CMakeFiles/example_bin.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mounika/MTP/sem/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/example_bin.dir/main.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/example_bin.dir/main.cpp.o -c /home/mounika/MTP/sem/main.cpp

CMakeFiles/example_bin.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/example_bin.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mounika/MTP/sem/main.cpp > CMakeFiles/example_bin.dir/main.cpp.i

CMakeFiles/example_bin.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/example_bin.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mounika/MTP/sem/main.cpp -o CMakeFiles/example_bin.dir/main.cpp.s

CMakeFiles/example_bin.dir/main.cpp.o.requires:

.PHONY : CMakeFiles/example_bin.dir/main.cpp.o.requires

CMakeFiles/example_bin.dir/main.cpp.o.provides: CMakeFiles/example_bin.dir/main.cpp.o.requires
	$(MAKE) -f CMakeFiles/example_bin.dir/build.make CMakeFiles/example_bin.dir/main.cpp.o.provides.build
.PHONY : CMakeFiles/example_bin.dir/main.cpp.o.provides

CMakeFiles/example_bin.dir/main.cpp.o.provides.build: CMakeFiles/example_bin.dir/main.cpp.o


# Object files for target example_bin
example_bin_OBJECTS = \
"CMakeFiles/example_bin.dir/main.cpp.o"

# External object files for target example_bin
example_bin_EXTERNAL_OBJECTS =

example_bin: CMakeFiles/example_bin.dir/main.cpp.o
example_bin: CMakeFiles/example_bin.dir/build.make
example_bin: /usr/lib/x86_64-linux-gnu/libGL.so
example_bin: glad/libglad.a
example_bin: glfw/src/libglfw3.a
example_bin: /usr/lib/x86_64-linux-gnu/librt.so
example_bin: /usr/lib/x86_64-linux-gnu/libm.so
example_bin: /usr/lib/x86_64-linux-gnu/libX11.so
example_bin: CMakeFiles/example_bin.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/mounika/MTP/sem/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable example_bin"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/example_bin.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/example_bin.dir/build: example_bin

.PHONY : CMakeFiles/example_bin.dir/build

CMakeFiles/example_bin.dir/requires: CMakeFiles/example_bin.dir/main.cpp.o.requires

.PHONY : CMakeFiles/example_bin.dir/requires

CMakeFiles/example_bin.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/example_bin.dir/cmake_clean.cmake
.PHONY : CMakeFiles/example_bin.dir/clean

CMakeFiles/example_bin.dir/depend:
	cd /home/mounika/MTP/sem/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mounika/MTP/sem /home/mounika/MTP/sem /home/mounika/MTP/sem/build /home/mounika/MTP/sem/build /home/mounika/MTP/sem/build/CMakeFiles/example_bin.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/example_bin.dir/depend

