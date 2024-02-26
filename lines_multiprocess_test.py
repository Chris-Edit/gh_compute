import compute_rhino3d.Util
import compute_rhino3d.Grasshopper as gh
import rhino3dm
import json
from rhino_token import token

compute_rhino3d.Util.url = "http://localhost:8081/"
compute_rhino3d.Util.authToken = token

pt1 = rhino3dm.Point3d(0, 0, 0)
circle = rhino3dm.Circle(pt1, 5)
angle = 20

# convert circle to curve and stringify
curve = json.dumps(circle.ToNurbsCurve().Encode())

# create list of input trees
curve_tree = gh.DataTree("RH_IN:curve")
curve_tree.Append([0], [curve])
rotate_tree = gh.DataTree("RH_IN:rotate")
rotate_tree.Append([0], [angle])
trees = [curve_tree, rotate_tree]

# output = gh.EvaluateDefinition('twisty.gh', trees)
def gh_run(_):
    return gh.EvaluateDefinition('twisty.gh', trees)


if __name__ == '__main__':

    import multiprocessing
    import time

    start = time.time()

    i = 100
    
    pool = multiprocessing.Pool(processes=6)
    pool.map(gh_run, range(100))
    pool.close()
    pool.join()
    

    # for i in range(100):
    #     gh_run(i)

    test = time.time() - start
    print(test * 10000)
