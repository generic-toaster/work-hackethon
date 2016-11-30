function roll() {
    var value = 0;
    var index = 0;
    var min = 20;
    //alert("here1");

    while(index++ < 4) {
        var v = -1;
        do {
            v = 1 + 1+Math.floor(Math.random()*5);
        } while(v < 1);

        if( v < min ) {
            min = v;
        }

        value += v;
        //alert(index + " - " + v + " val = " + value + " min = " + min)
    }

    return (value - min);
}