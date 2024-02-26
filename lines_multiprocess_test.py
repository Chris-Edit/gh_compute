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

    # pool = multiprocessing.Pool(processes=6)
    # pool.map(gh_run, range(100))
    # pool.close()
    # pool.join()
    

    for i in range(100):
        gh_run(i)



    test = time.time() - start
    print(test * 10000)

    # with multiprocessing.Pool(processes=2) as pool:
    #     outputs = pool.starmap(gh_run, ['twisty.gh'])

    # import time
    # start = time.time()
    # 
    # for _ in range(8):
    #     output = gh_run('twisty.gh')
    # 
    # print((time.time() - start) * 100000)

    # decode results
    # output = outputs[0]
    # branch = output['values'][0]['InnerTree']['{0;0}']
    # lines = [rhino3dm.CommonObject.Decode(json.loads(item['data'])) for item in branch]
    # 
    # filename = 'twisty.3dm'
    # 
    # print('Writing {} lines to {}'.format(len(lines), filename))
    # 
    # # create a 3dm file with results
    # model = rhino3dm.File3dm()
    # for l in lines:
    #     model.Objects.AddCurve(l) # they're actually LineCurves...
    # 
    # model.Write(filename)
