import argparse
from pathlib import Path

from huggingface_hub import snapshot_download


def main():
    parser = argparse.ArgumentParser(
        description="Download the full dataset folder from Hugging Face."
    )
    parser.add_argument(
        "--repo-id",
        required=True,
        help="Example: nethsith/sri-lankan-album-stamp-detection",
    )
    parser.add_argument(
        "--output-dir",
        default="data",
        help="Local folder to save the dataset into. Default: data",
    )
    parser.add_argument(
        "--token",
        default=None,
        help="Optional Hugging Face token. Normally not needed after `hf auth login`.",
    )
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parents[1]
    output_dir = (project_root / args.output_dir).resolve()

    print(f"Downloading dataset: {args.repo_id}")
    print(f"Saving into:        {output_dir}")

    snapshot_download(
        repo_id=args.repo_id,
        repo_type="dataset",
        local_dir=str(output_dir),
        token=args.token,
    )

    print("\nDownload completed successfully.")

    # Optional structure checks
    expected_paths = [
        output_dir / "yolo_dataset" / "images" / "train",
        output_dir / "yolo_dataset" / "images" / "val",
        output_dir / "yolo_dataset" / "labels" / "train",
        output_dir / "yolo_dataset" / "labels" / "val",
    ]

    missing = [str(path) for path in expected_paths if not path.exists()]

    if missing:
        print("\nWarning: Download finished, but these expected YOLO folders were not found:")
        for path in missing:
            print(f"  - {path}")
    else:
        print("\nYOLO dataset structure verified.")


if __name__ == "__main__":
    main()