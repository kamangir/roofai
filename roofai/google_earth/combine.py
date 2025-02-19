import glob
from tqdm import tqdm
from pygltflib import GLTF2, Scene, Node


def combine_glbs(output_file="combined.glb"):
    combined_gltf = GLTF2()
    combined_gltf.scenes = [Scene(nodes=[])]
    combined_gltf.nodes = []

    for filename in tqdm(glob.glob("*.glb")):

        if filename == "combined.glb":
            continue

        gltf = GLTF2().load(filename)

        # Assume one scene per file for simplicity
        scene_index = gltf.scene or 0
        scene = gltf.scenes[scene_index]

        for node_index in scene.nodes:
            node = gltf.nodes[node_index]
            combined_gltf.nodes.append(node)
            combined_gltf.scenes[0].nodes.append(len(combined_gltf.nodes) - 1)

    # Only save the combined GLTF to a file if there were any .glb files processed
    if combined_gltf.nodes:
        combined_gltf.save(output_file)
        print(f"-> {output_file}")


if __name__ == "__main__":
    combine_glbs()
