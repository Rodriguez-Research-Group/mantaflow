# In:
#  OPENVDB_ROOT
#
# Out:
#  OPENVDB_FOUND
#  OPENVDB_INCLUDE_DIRS
#  OPENVDB_LIBRARY_DIRS
#  OPENVDB_DEFINITIONS

if(NOT OPENVDB_ROOT)
	if(IS_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/openVDB")
		set(OPENVDB_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/openVDB")
	endif()
else()
	set(OPENVDB_ROOT "" CACHE PATH "OpenVDB base path")
endif()

if(OPENVDB_ROOT)
	set(OPENVDB_INCLUDE_DIR "${OPENVDB_ROOT}/include" CACHE PATH "Include files for openVDB")
	set(OPENVDB_LIBRARY_DIR "${OPENVDB_ROOT}/lib" CACHE PATH "OpenVDB libraries")
	set(OPENVDB_LIBRARY "${OPENVDB_LIBRARY_DIR}/openVDB.lib" CACHE FILEPATH "OpenVDB library filepath")
	set(OPENVDB_DEFINITIONS "")
	list(APPEND OPENVDB_DEFINITIONS -DOPENVDB_DLL)
	list(APPEND OPENVDB_DEFINITIONS -DOPENVDB_3_ABI_COMPATIBLE)
	set(OPENVDB_FOUND TRUE)
endif()