import subprocess

def get_gcloud_versions():
    # Run the gcloud command and capture the output
    result = subprocess.run(
        ['gcloud', 'app', 'versions', 'list', '--format=value(version.id)', '--sort-by=~version.createTime'],
        stdout=subprocess.PIPE,
        text=True
    )
    # Split the output into a list of version IDs
    versions = result.stdout.strip().split('\n')
    return versions

def delete_gcloud_version(version_id):
    # Run the gcloud command to delete the specified version
    subprocess.run(['gcloud', 'app', 'versions', 'delete', version_id, '-q'])

def main():
    # Get all version IDs sorted by creation time, newest first
    versions = get_gcloud_versions()

    # Keep the latest two versions and delete the rest
    for version in versions[2:]:
        delete_gcloud_version(version)

if __name__ == "__main__":
    main()
