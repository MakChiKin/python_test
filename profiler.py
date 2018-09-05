import maya.cmds as cmds

# Start profiling
cmds.profiler(sampling = True)

# Wait for events to be profiled
# Stop profiling
cmds.profiler(sampling = False)

# 将结果输出到文件
cmds.profiler(output = "test.txt")

# 将记录从文件加载到缓冲区
cmds.profiler(load = "test.txt")

# Reset the tool
cmds.profiler(reset = True)

# Set the profiler's buffer size to fit 5 megaBytes
cmds.profiler(bufferSize = 5)

# Query the profiler's buffer size
cmds.profiler(query = True, bufferSize = True)

# Add a new category
cmds.profiler(addCategory = "Test Category")

# Remove an existing category
cmds.profiler(removeCategory = "Test Category")

# Query the number of categories
cmds.profiler(query = True, categoryCount = True)

# Query the name of the category at the given index
cmds.profiler(query = True, categoryIndexToName  = 5)

# Query the index of the category with the given name
cmds.profiler(query = True, categoryNameToIndex = "Maya Qt")

# Query if it is enabled for the recording of the category at the given index
cmds.profiler(query = True, categoryRecording = True, categoryIndex = 5)

# Query if it is enabled for the recording of the category with the given name
cmds.profiler(query = True, categoryRecording = True, categoryName = "Maya Qt")

# Enable/Disable the recording of the category at the given index
cmds.profiler(categoryRecording = False, categoryIndex = 5)

# Query the number of the events in the buffer
cmds.profiler(query = True, eventCount = True)

# Query the time at which the event at the given index start
cmds.profiler(query = True, eventStartTime = True, eventIndex = 100)

# Query the duration of the event at the given index
cmds.profiler(query = True, eventDuration = True, eventIndex = 100)

# Query the name of the event at the given index
cmds.profiler(query = True, eventName = True, eventIndex = 100)

# Query the description of the event at the given index
cmds.profiler(query = True, eventDescription = True, eventIndex = 100)

# Query the category the the event at the given index belongs to
cmds.profiler(query = True, eventCategory = True, eventIndex = 100)

# Query the color of the event at the given index
cmds.profiler(query = True, eventColor = True, eventIndex = 100)

# Query the thread ID of the event at the given index
cmds.profiler(query = True, eventThreadId = True, eventIndex = 100)

# Query the CPU ID of the event at the given index
cmds.profiler(query = True, eventCPUId = True, eventIndex = 100)

# Query if the event at the given index is a signal event
cmds.profiler(query = True, signalEvent = True, eventIndex = 100)