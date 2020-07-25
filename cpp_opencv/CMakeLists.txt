cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(aopencv)

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/bin)

find_package(OpenCV REQUIRED)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")

set(SRC_LIST main.cpp utils.cpp demo.cpp test.cpp)
# set(SRC_LIST main.cpp)

add_executable(${PROJECT_NAME} ${SRC_LIST})

target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})
set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 14)
