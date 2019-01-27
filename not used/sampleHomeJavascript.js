function order(data){
    var newData = []
	for(var i = 0; i < data.length; i++){
		var newDataValue = parse(data[i]);
        var upvotes = newDataValue[0];
        var repstat = newDataValue[1];
        var repnum = newDataValue[2];
        var ansstat = newDataValue[3];
        var ansnum = newDataValue[4];
        var answers = [];
        for(var a = 0; i < ansnum; i++){
          answers[i] = newDataValue[4 + i];
        }
    }
}

function parse(data){
    var newData = data.split(".");
    return newData;
}

var info = parse("32.0.23.1.2.yep.ok");
console.log(info);
