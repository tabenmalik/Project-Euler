cmake_minimum_required (VERSION 3.3.0)

set (CMAKE_CXX_STANDARD 11)
set (
    CMAKE_HOME_DIRECTORY
    ${CMAKE_HOME_DIRECTORY}
)
set (
    CMAKE_RUNTIME_OUTPUT_DIRECTORY
    ${CMAKE_BINARY_DIR}/bin
)

project (euler)

macro (subdirlist result curdir)
    file (GLOB children RELATIVE ${curdir} ${curdir}/*)
    set (dirlist "")
    foreach (child ${children})
        if (IS_DIRECTORY ${curdir}/${child})
            list (APPEND dirlist ${child})
        endif()
    endforeach()
    set (${result} ${dirlist})
endmacro (subdirlist)

subdirlist (problems "${CMAKE_CURRENT_SOURCE_DIR}/src")

foreach (problem ${problems})
    add_executable(${problem} ${CMAKE_CURRENT_SOURCE_DIR}/src/${problem}/${problem}.cpp)
endforeach()