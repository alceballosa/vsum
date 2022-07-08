# vsum

```bash
conda activate torch_zoo
```

```bash
nohup python -u main.py \
    feature_type=i3d \
    flow_type=raft \
    streams=rgb \
    device_ids="[0]" \
    file_with_video_paths=/home/alberto/workspace/video-summarization/vsum-repo/local/videos_list.txt \
    output_path=/home/alberto/workspace/video-summarization/datasets/tv-sum/extracted_features \
    on_extraction=save_numpy \
    stack_size=60 \
    step_size=1 > feature_extraction_i92.out 2>&1 &
```