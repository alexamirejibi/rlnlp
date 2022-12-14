import csv
import pickle
from utils import ACTION_WORDS

with open('data/new_augmented_data_5_labels.pkl', 'rb') as d:
    data = pickle.load(d)

header = ['description', 'label', 'short_traj'] + ACTION_WORDS

data_d = []

with open('data/new_augmented_data.csv', 'w', newline='') as f:
    # create the csv writer
    writer = csv.writer(f)
    writer.writerow(header)
    for i in data:
        tmp = [i['sentence'], i['label'], i['short_traj'], i['action_freqs'][0], i['action_freqs'][1], i['action_freqs'][2], i['action_freqs'][3], i['action_freqs'][4], i['action_freqs'][5], i['action_freqs'][6], i['action_freqs'][7], i['action_freqs'][8], i['action_freqs'][9], i['action_freqs'][10], i['action_freqs'][11], i['action_freqs'][12], i['action_freqs'][13], i['action_freqs'][14], i['action_freqs'][15], i['action_freqs'][16], i['action_freqs'][17]]
        assert len(tmp) == len(header)
        writer.writerow(tmp)