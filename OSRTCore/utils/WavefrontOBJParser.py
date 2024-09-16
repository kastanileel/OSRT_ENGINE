import taichi as ti
import taichi.math as tm

from OSRTCore.raytracer.primitives import Triangle


class WavefrontOBJParser:
    """Wavefront OBJ parser

    This class is used to parse Wavefront OBJ files and its associated MTL files.
    """

    @staticmethod
    def parse(file_path):
        obj = open(file_path)
        lines = obj.readlines()

        vertices = []
        triangles = []
        for line in lines:
            # remove whitespaces
            line.strip()
            if line.startswith("v "):
                elements = line.split()
                vertices.append(tm.vec3(float(elements[1]), float(elements[2]), float(elements[3])))
            elif line.startswith("f"):
                elements = line.split()

                # TODO: cleanup, this is for debugging/testing only:
                if "/" in elements[1]:
                    elements[1] = elements[1].strip("/")[0]
                    elements[2] = elements[2].strip("/")[0]
                    elements[3] = elements[3].strip("/")[0]

                triangles.append(Triangle(vertices[int(elements[1])-1],
                                          vertices[int(elements[2])-1],
                                          vertices[int(elements[3])-1]))
        return triangles
