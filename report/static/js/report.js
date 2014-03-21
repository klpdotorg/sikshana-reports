var detail=new Array();
var flag='math';
var def=math;
var select_type='state';
var select_clas=clas[0];
var total = new Array();

function createOption(dropdown, text, value) {
    var opt = document.createElement('option');
    opt.value = value;
    opt.text = text;
    dropdown.appendChild(opt);
}

for(i=0;i<dist.length;i++){
    createOption(document.getElementById('district'),dist[i],dist[i]);
}
for(i=0;i<clas.length;i++){
  createOption(document.getElementById('clas'),clas[i],clas[i]);
}

function filldropdown(type,value){
    document.getElementById('alldistrict').style.visibility="visible";
    var data=new Array();
    if(type=='block'){
        data=blck;
        document.getElementById('block').length=1;
        document.getElementById('cluster').length=1;
        document.getElementById('school').length=1;
      }
    else if(type=='cluster'){
        data=clst;
        document.getElementById('cluster').length=1;
        document.getElementById('school').length=1;
      }
    else if(type=='school'){
        data=schl;
        document.getElementById('school').length=1;
      }
    dropdown=document.getElementById(type);
    dropdown.length=1;
    for(i=0;i<data.length;i++){
        if(value.trim()==data[i][0].trim()){
            createOption(dropdown,data[i][1],data[i][1]);
        }
    }
}


function getdata(clas,type) {
  if(type!=''){
    select_type=type;
  }
  if(clas!=''){
    select_clas=clas;
  }

  document.getElementById('type').value=select_type;
  var values = $('#form1').serialize();
  
  $.ajax({
      type: "POST",
      url: '/',
      data: values,
      success: function(response){ 
    detail=new Array();
    for(i=0;i<response[0].length;i++){
      detail.push(response[0][i].split('|'));
      detail[i].push(response[1][i].split('|')[2]);
      if(response[0][i].split('|')[0]=='total'){
	      total[0]=response[0][i].split('|')[1];
        total[1]=response[1][i].split('|')[1];
      }
    }
    drawChart(flag,def);
      },
      error: function (xhr, ajaxOptions, thrownError) {
            alert(xhr.status);
          alert(thrownError);
      alert("Error");
        }
  });
}

var cssClassNames={
  'tableRow': 'table-row',
  'oddTableRow':'table-row table-row-odd',
  'headerRow': 'table-header'
}

google.load("visualization", "1", {packages:["corechart","table"]});
google.setOnLoadCallback(callback);
function callback(){
    getdata(clas,'All District');
}

function drawChart(ctype, opt) {
  parent={'All District':'All District','district':'All District','block':'District','cluster':'Block','school':'Cluster'}
  var data1 = new google.visualization.DataTable();
  data1.addColumn('string', 'Subject');
  if(select_type!='All District'){
    data1.addColumn('string', parent[select_type] + ' : ' + total[1] + ' Students');  
  }
  data1.addColumn('string', select_type.charAt(0).toUpperCase() + select_type.slice(1) + ' : ' + total[0] + ' Students');

  var data2 = new google.visualization.DataTable();
  data2.addColumn('string', 'subject');
  if(select_type!='All District'){
  	data2.addColumn('number', parent[select_type] + ' Total Students ' + ' : ' + total[1]);
  	data2.addColumn({type: 'string', role: 'tooltip'});
  }
  data2.addColumn('number', select_type.charAt(0).toUpperCase() + select_type.slice(1) + ' Total Students ' + ' : ' + total[0]);
  data2.addColumn({type: 'string', role: 'tooltip'});

  if(ctype!='')
	  flag=ctype;
  def=opt;
  var temp1=new Array();
	  var temp2=new Array();
  for(i=0;i<opt.length;i++){
    temp1=temp2=[opt[i],0,0];
    for(j=0;j<detail.length;j++){
      if(detail[j][0].trim()==flag && detail[j][1]==opt[i]){
        //alert(detail[j]);
        temp1=[detail[j][1].trim(), String(parseFloat(detail[j][3])) + '%'];
        temp2=[detail[j][1].trim(), parseFloat(detail[j][3]), parent[select_type] + ' : ' + parseFloat(detail[j][3]) + '%'];  
        if(select_type!='All District'){
            temp1.push(String(parseFloat(detail[j][2])) + '%');
            temp2.push(parseFloat(detail[j][2]));
            temp2.push(select_type.charAt(0).toUpperCase() + select_type.slice(1) + ' : ' + String(parseFloat(detail[j][2])) + '%');
        }
        break;
      }
    }
    data1.addRow(temp1);
    data2.addRow(temp2);
  }
  var view = new google.visualization.DataView(data2);
  var setcolumn=[0, 1, 2,
                    { calc: "stringify",
                      sourceColumn: 1,
                      type: "string",
                      role: "annotation" }];
  if(select_type!='All District'){
  setcolumn.push(3);
  setcolumn.push(4);
  setcolumn.push({ calc: "stringify",
                      sourceColumn: 3,
                      type: "string",
                      role: "annotation" });
}
view.setColumns(setcolumn);	
          var options = {
          'title':'',
          'allowHtml':true,
          'cssClassNames':cssClassNames,
          'legend': {position:'right'},
          'vAxis':{minvalue:0, maxValue:100, title:'Percentage'},
          'colors':['#005D6E','#42A5B3']
          };

	var change_chart=document.getElementById('change_chart');
  var table_chart=document.getElementById('table_chart_div');
  var bar_chart=document.getElementById('bar_chart_div');
  document.getElementById('count').style.display='block';
	if(change_chart.value=='Bar-Chart' && ctype==''){
    var chart = new google.visualization.ColumnChart(bar_chart);
    data=view;
    bar_chart.style.display='block';
    table_chart.style.display='none';
	  change_chart.value='Table-Chart';
    change_chart.src='/home/brijesh/sikshana_report/report/static/css/1391795212_229119.ico';
	}
	else if(change_chart.value=='Table-Chart' && ctype==''){
	  var chart = new google.visualization.Table(table_chart);
    data=data1;
    bar_chart.style.display='none';
    table_chart.style.display='block';
	  change_chart.value='Bar-Chart';
    change_chart.src='/home/brijesh/sikshana_report/report/static/css/barchart_multicolor.ico';
	}
	else if(change_chart.value=='Table-Chart' && ctype!=''){
	  var chart = new google.visualization.ColumnChart(bar_chart);
    data=view;
    bar_chart.style.display='block';
    table_chart.style.display='none';
  }
	else{
 	  var chart = new google.visualization.Table(table_chart);
    data=data1;
    bar_chart.style.display='none';
    table_chart.style.display='block';
  }

    chart.draw(data, options);
}

function popup(){
  element=document.getElementById('popup');
  if(element.style.display=='none')
    element.style.display='block'
  else
 	   element.style.display='none'
}
