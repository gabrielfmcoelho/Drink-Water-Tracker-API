# extract-openapi.py
import argparse
import json
import sys
import yaml
from uvicorn.importer import import_from_string
from app import DocsSchema
import os

parser = argparse.ArgumentParser(prog="extract-openapi.py")
parser.add_argument("app",       help='App import string. Eg. "main:app"', default="app:api")
parser.add_argument("--app-dir", help="Directory containing the app", default=None)
parser.add_argument("--out",     help="Output file ending in .json or .yaml", default="openapi.yaml")
parser.add_argument("--out-dir", help="Output directory for the doc file", default="./docs/")

if __name__ == "__main__":
    args = parser.parse_args()

    if args.app_dir is not None:
        print(f"adding {args.app_dir} to sys.path")
        sys.path.insert(0, args.app_dir)

    print(f"importing app from {args.app}")
    app = import_from_string(args.app)
    openapi = DocsSchema.get_docs()
    version = openapi.get("openapi", "unknown version")
    
    final_path = args.out_dir+args.out

    print(f"writing openapi spec v{version}")
    with open(final_path, "w") as f:
        if args.out.endswith(".json"):
            json.dump(openapi, f, indent=2)
        else:
            yaml.dump(openapi, f, sort_keys=False)

    print(f"spec written to {args.out}")