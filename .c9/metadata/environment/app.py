{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":52,"position":52,"stack":[[{"start":{"row":31,"column":41},"end":{"row":32,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"insert","lines":["    "]},{"start":{"row":32,"column":4},"end":{"row":33,"column":0},"action":"insert","lines":["",""]},{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"insert","lines":["    "]},{"start":{"row":33,"column":4},"end":{"row":34,"column":0},"action":"insert","lines":["",""]},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"insert","lines":["    "]},{"start":{"row":34,"column":4},"end":{"row":35,"column":0},"action":"insert","lines":["",""]},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":35,"column":4},"end":{"row":35,"column":13},"action":"insert","lines":["view_revu"],"id":3}],[{"start":{"row":34,"column":0},"end":{"row":40,"column":53},"action":"insert","lines":["# Edit task","@app.route('/edit_task/<task_id>')","def edit_task(task_id):","    the_task =  mongo.db.tasks.find_one({\"_id\": ObjectId(task_id)})","    all_categories =  mongo.db.categories.find()","    return render_template('edittask.html', task=the_task,","                           categories=all_categories)"],"id":4}],[{"start":{"row":41,"column":4},"end":{"row":41,"column":13},"action":"remove","lines":["view_revu"],"id":5},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"remove","lines":["    "]},{"start":{"row":40,"column":57},"end":{"row":41,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":35,"column":13},"end":{"row":35,"column":22},"action":"remove","lines":["edit_task"],"id":6},{"start":{"row":35,"column":13},"end":{"row":35,"column":22},"action":"insert","lines":["view_revu"]}],[{"start":{"row":35,"column":24},"end":{"row":35,"column":31},"action":"remove","lines":["task_id"],"id":7},{"start":{"row":35,"column":24},"end":{"row":35,"column":25},"action":"insert","lines":["r"]},{"start":{"row":35,"column":25},"end":{"row":35,"column":26},"action":"insert","lines":["e"]},{"start":{"row":35,"column":26},"end":{"row":35,"column":27},"action":"insert","lines":["v"]},{"start":{"row":35,"column":27},"end":{"row":35,"column":28},"action":"insert","lines":["i"]},{"start":{"row":35,"column":28},"end":{"row":35,"column":29},"action":"insert","lines":["e"]},{"start":{"row":35,"column":29},"end":{"row":35,"column":30},"action":"insert","lines":["w"]}],[{"start":{"row":35,"column":24},"end":{"row":35,"column":30},"action":"remove","lines":["review"],"id":8},{"start":{"row":35,"column":24},"end":{"row":35,"column":33},"action":"insert","lines":["review_id"]}],[{"start":{"row":36,"column":14},"end":{"row":36,"column":21},"action":"remove","lines":["task_id"],"id":9},{"start":{"row":36,"column":14},"end":{"row":36,"column":23},"action":"insert","lines":["review_id"]}],[{"start":{"row":36,"column":4},"end":{"row":36,"column":13},"action":"remove","lines":["edit_task"],"id":10},{"start":{"row":36,"column":4},"end":{"row":36,"column":13},"action":"insert","lines":["view_revu"]}],[{"start":{"row":34,"column":2},"end":{"row":34,"column":11},"action":"remove","lines":["Edit task"],"id":11},{"start":{"row":34,"column":2},"end":{"row":34,"column":3},"action":"insert","lines":["V"]},{"start":{"row":34,"column":3},"end":{"row":34,"column":4},"action":"insert","lines":["i"]},{"start":{"row":34,"column":4},"end":{"row":34,"column":5},"action":"insert","lines":["e"]},{"start":{"row":34,"column":5},"end":{"row":34,"column":6},"action":"insert","lines":["w"]}],[{"start":{"row":34,"column":6},"end":{"row":34,"column":7},"action":"insert","lines":[" "],"id":12},{"start":{"row":34,"column":7},"end":{"row":34,"column":8},"action":"insert","lines":["R"]},{"start":{"row":34,"column":8},"end":{"row":34,"column":9},"action":"insert","lines":["e"]},{"start":{"row":34,"column":9},"end":{"row":34,"column":10},"action":"insert","lines":["v"]}],[{"start":{"row":34,"column":10},"end":{"row":34,"column":11},"action":"insert","lines":["u"],"id":13}],[{"start":{"row":34,"column":10},"end":{"row":34,"column":11},"action":"remove","lines":["u"],"id":14},{"start":{"row":34,"column":9},"end":{"row":34,"column":10},"action":"remove","lines":["v"]},{"start":{"row":34,"column":8},"end":{"row":34,"column":9},"action":"remove","lines":["e"]}],[{"start":{"row":34,"column":8},"end":{"row":34,"column":9},"action":"insert","lines":["E"],"id":15},{"start":{"row":34,"column":9},"end":{"row":34,"column":10},"action":"insert","lines":["V"]},{"start":{"row":34,"column":10},"end":{"row":34,"column":11},"action":"insert","lines":["U"]}],[{"start":{"row":37,"column":4},"end":{"row":37,"column":12},"action":"remove","lines":["the_task"],"id":16},{"start":{"row":37,"column":4},"end":{"row":37,"column":5},"action":"insert","lines":["r"]},{"start":{"row":37,"column":5},"end":{"row":37,"column":6},"action":"insert","lines":["e"]},{"start":{"row":37,"column":6},"end":{"row":37,"column":7},"action":"insert","lines":["v"]},{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"insert","lines":["u"]}],[{"start":{"row":37,"column":4},"end":{"row":37,"column":5},"action":"insert","lines":["t"],"id":17},{"start":{"row":37,"column":5},"end":{"row":37,"column":6},"action":"insert","lines":["h"]},{"start":{"row":37,"column":6},"end":{"row":37,"column":7},"action":"insert","lines":["e"]},{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"insert","lines":["_"]}],[{"start":{"row":37,"column":25},"end":{"row":37,"column":30},"action":"remove","lines":["tasks"],"id":18},{"start":{"row":37,"column":25},"end":{"row":37,"column":32},"action":"insert","lines":["reviews"]}],[{"start":{"row":37,"column":59},"end":{"row":37,"column":66},"action":"remove","lines":["task_id"],"id":19},{"start":{"row":37,"column":59},"end":{"row":37,"column":68},"action":"insert","lines":["review_id"]}],[{"start":{"row":38,"column":4},"end":{"row":38,"column":48},"action":"remove","lines":["all_categories =  mongo.db.categories.find()"],"id":20},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":37,"column":71},"end":{"row":38,"column":0},"action":"remove","lines":["",""],"id":21}],[{"start":{"row":38,"column":57},"end":{"row":39,"column":52},"action":"remove","lines":[",","                           categories=all_categories"],"id":22}],[{"start":{"row":38,"column":44},"end":{"row":38,"column":48},"action":"remove","lines":["task"],"id":23},{"start":{"row":38,"column":44},"end":{"row":38,"column":45},"action":"insert","lines":["r"]},{"start":{"row":38,"column":45},"end":{"row":38,"column":46},"action":"insert","lines":["e"]},{"start":{"row":38,"column":46},"end":{"row":38,"column":47},"action":"insert","lines":["v"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"insert","lines":["u"]}],[{"start":{"row":38,"column":49},"end":{"row":38,"column":57},"action":"remove","lines":["the_task"],"id":24},{"start":{"row":38,"column":49},"end":{"row":38,"column":50},"action":"insert","lines":["t"]},{"start":{"row":38,"column":50},"end":{"row":38,"column":51},"action":"insert","lines":["h"]},{"start":{"row":38,"column":51},"end":{"row":38,"column":52},"action":"insert","lines":["e"]}],[{"start":{"row":38,"column":49},"end":{"row":38,"column":52},"action":"remove","lines":["the"],"id":25},{"start":{"row":38,"column":49},"end":{"row":38,"column":57},"action":"insert","lines":["the_revu"]}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"insert","lines":["#"],"id":26}],[{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"insert","lines":[" "],"id":27},{"start":{"row":12,"column":2},"end":{"row":12,"column":3},"action":"insert","lines":["H"]}],[{"start":{"row":12,"column":3},"end":{"row":12,"column":4},"action":"insert","lines":["o"],"id":28},{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["m"]},{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"insert","lines":["e"]}],[{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"insert","lines":[" "],"id":29},{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"insert","lines":["/"]}],[{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":[" "],"id":30},{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"insert","lines":["i"]},{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"insert","lines":["n"]},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["d"]},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"insert","lines":["e"]},{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"insert","lines":["x"]}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "],"id":31}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"insert","lines":["#"],"id":32}],[{"start":{"row":18,"column":1},"end":{"row":18,"column":2},"action":"insert","lines":[" "],"id":33},{"start":{"row":18,"column":2},"end":{"row":18,"column":3},"action":"insert","lines":["U"]},{"start":{"row":18,"column":3},"end":{"row":18,"column":4},"action":"insert","lines":["s"]},{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"insert","lines":["e"]},{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"insert","lines":["r"]}],[{"start":{"row":18,"column":6},"end":{"row":18,"column":7},"action":"insert","lines":[" "],"id":34},{"start":{"row":18,"column":7},"end":{"row":18,"column":8},"action":"insert","lines":["a"]},{"start":{"row":18,"column":8},"end":{"row":18,"column":9},"action":"insert","lines":["g"]},{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"insert","lines":["r"]},{"start":{"row":18,"column":10},"end":{"row":18,"column":11},"action":"insert","lines":["e"]},{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"insert","lines":["e"]},{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"insert","lines":["m"]},{"start":{"row":18,"column":13},"end":{"row":18,"column":14},"action":"insert","lines":["e"]},{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":["n"]},{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"remove","lines":["    "],"id":35}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":1},"action":"insert","lines":["#"],"id":36}],[{"start":{"row":23,"column":1},"end":{"row":23,"column":2},"action":"insert","lines":[" "],"id":37},{"start":{"row":23,"column":2},"end":{"row":23,"column":3},"action":"insert","lines":["S"]},{"start":{"row":23,"column":3},"end":{"row":23,"column":4},"action":"insert","lines":["i"]},{"start":{"row":23,"column":4},"end":{"row":23,"column":5},"action":"insert","lines":["g"]},{"start":{"row":23,"column":5},"end":{"row":23,"column":6},"action":"insert","lines":["n"]}],[{"start":{"row":23,"column":6},"end":{"row":23,"column":7},"action":"insert","lines":[" "],"id":38},{"start":{"row":23,"column":7},"end":{"row":23,"column":8},"action":"insert","lines":["i"]},{"start":{"row":23,"column":8},"end":{"row":23,"column":9},"action":"insert","lines":["n"]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"remove","lines":["    "],"id":39}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":1},"action":"insert","lines":["S"],"id":40},{"start":{"row":28,"column":1},"end":{"row":28,"column":2},"action":"insert","lines":["i"]},{"start":{"row":28,"column":2},"end":{"row":28,"column":3},"action":"insert","lines":["g"]},{"start":{"row":28,"column":3},"end":{"row":28,"column":4},"action":"insert","lines":["n"]}],[{"start":{"row":28,"column":4},"end":{"row":28,"column":5},"action":"insert","lines":[" "],"id":41},{"start":{"row":28,"column":5},"end":{"row":28,"column":6},"action":"insert","lines":["u"]},{"start":{"row":28,"column":6},"end":{"row":28,"column":7},"action":"insert","lines":["p"]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":1},"action":"insert","lines":["#"],"id":42}],[{"start":{"row":28,"column":1},"end":{"row":28,"column":2},"action":"insert","lines":[" "],"id":43}],[{"start":{"row":27,"column":2},"end":{"row":27,"column":3},"action":"remove","lines":[" "],"id":44},{"start":{"row":27,"column":1},"end":{"row":27,"column":2},"action":"remove","lines":[" "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":27,"column":0},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":45}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"remove","lines":["    "],"id":46}],[{"start":{"row":22,"column":0},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":47}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "],"id":48}],[{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":49}],[{"start":{"row":10,"column":20},"end":{"row":11,"column":0},"action":"remove","lines":["",""],"id":50}],[{"start":{"row":10,"column":20},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":51},{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":42,"column":28},"end":{"row":42,"column":36},"action":"remove","lines":["edittask"],"id":52},{"start":{"row":42,"column":28},"end":{"row":42,"column":29},"action":"insert","lines":["r"]},{"start":{"row":42,"column":29},"end":{"row":42,"column":30},"action":"insert","lines":["e"]},{"start":{"row":42,"column":30},"end":{"row":42,"column":31},"action":"insert","lines":["v"]},{"start":{"row":42,"column":31},"end":{"row":42,"column":32},"action":"insert","lines":["u"]}],[{"start":{"row":42,"column":43},"end":{"row":42,"column":44},"action":"remove","lines":["u"],"id":53}],[{"start":{"row":42,"column":43},"end":{"row":42,"column":44},"action":"insert","lines":["i"],"id":54},{"start":{"row":42,"column":44},"end":{"row":42,"column":45},"action":"insert","lines":["e"]},{"start":{"row":42,"column":45},"end":{"row":42,"column":46},"action":"insert","lines":["w"]}]]},"ace":{"folds":[],"scrolltop":300,"scrollleft":0,"selection":{"start":{"row":23,"column":40},"end":{"row":23,"column":40},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":7,"state":"start","mode":"ace/mode/python"}},"timestamp":1575502724300,"hash":"4e62f4a561b075f5e5fef98e379ed0454680ab18"}