from fuctions_lab2 import read_file, get_frame_sync, get_channel_information, write_file

flujoE1 = read_file("flujoE1.txt")
FAS = "0011011"
frame_sync_index = get_frame_sync(text=flujoE1, frame_sync=FAS)
channel_information = get_channel_information(
    text=flujoE1, channel=13, frame_sync_index=frame_sync_index
)
write_file(output_file_name="decoded_text", text_to_write=channel_information)
