from flask import Flask, request, abort, send_from_directory, jsonify
from pathlib import Path

api = Flask(__name__)
api.config['UPLOAD_FOLDER'] = Path(__file__).parent.parent / "files"
#current_path = os.path.dirname(os.path.realpath(__file__))
#UPLOAD_DIRECTORY = os.path.join( "files")

print(api.config['UPLOAD_FOLDER'])


@api.route("/files/<path:path>", methods=["GET"])
def get_file(path):
    """Download a file."""
    return send_from_directory(api.config['UPLOAD_FOLDER'], path, as_attachment=False)


@api.route("/files/<filename>", methods=["PUT"])
def add_file(filename):
    """Upload a file."""

    if "/" in filename:
        # Return 400 BAD REQUEST
        abort(400, "no subdirectories directories allowed")

    file_path = api.config['UPLOAD_FOLDER'] / filename
    with open(file_path, "wb") as fp:
        fp.write(request.data)

    # Return 201 CREATED
    return "", 201


@api.route("/files/<filename>", methods=["DELETE"])
def delete_file(filename):
    print("Access to", filename, "requested")

    file_path = api.config['UPLOAD_FOLDER'] / filename
    # checking whether file exists or not
    if os.path.exists(file_path):
        os.remove(file_path)
        print("File deleted")
        return "", 200
    else:
        # file not found message
        print("File not found in the directory")
        return "", 404


@api.route("/files", methods=["GET"])
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(api.config['UPLOAD_FOLDER']):
        file_path = api.config['UPLOAD_FOLDER'] / filename
        if os.path.isfile(file_path):
            files.append(filename)
    return jsonify(files), 200


if __name__ == '__main__':
    api.run(debug=True, port=5000)
