var ExcelToJSON = function () {
  var currentURL = window.location.href;
alert(currentURL);
  switch(currentURL) {
    case 'http://localhost:8000/inventory':
      //alert("Inventory batch update completed");
      break;
    case 'http://localhost:8000/customersku':
      alert("CustomerSKU batch update completed");
      break;
    default:
      // code block
  }

  if (currentURL.includes('/inventory')) 
  {
    alert("Inventory batch update completed");
  }

  this.parseExcel = function (file) {
    var reader = new FileReader();
    reader.onload = function (e) {
      var data = e.target.result;
      var workbook = XLSX.read(data, {
        type: 'binary'
      });
      workbook.SheetNames.forEach(function (sheetName) {
        // Here is your object
        var XL_row_object = XLSX.utils.sheet_to_row_object_array(workbook.Sheets[sheetName]);
        var json_object = JSON.stringify(XL_row_object);
        console.log(JSON.parse(json_object));
        jQuery('#xlx_json').val(json_object);

        //Base on the current url to update inventory or customersku or...

        switch(currentURL) {
          case 'http://localhost:8000/inventory':
              //update the inventory by json
          // $.ajax({
          //   // url: 'ajaxUpdateInventory_Byjson/',
          //   url: 'ajaxUpdateInventory_Byjson/',
          //   data: {
          //     'jsonValue': json_object

          //   },
          //   success: function (data) {
          //     $("#idImg").html(data);
          //   }
          // });
          callAjaxByURL('ajaxUpdateInventory_Byjson/');
          //end update inventory
            break;
          case 'http://localhost:8000/customersku':
            alert("CustomerSKU batch update completed");
            break;
          default:
            // code block
        }

        
      })
    };
    reader.onerror = function (ex) {
      console.log(ex);
    };
    reader.readAsBinaryString(file);
  };

};
function handleFileSelect(evt) {
  var files = evt.target.files; // FileList object
  var xl2json = new ExcelToJSON();
  xl2json.parseExcel(files[0]);

  refresh();
}

function refresh() {
  setTimeout(function () {
    location.reload()
  }, 300);
}

function UpdateInventory(clicked_id) {
  var Qty = document.getElementById('QualityOnHold_' + clicked_id).value;
  alert(clicked_id + " qty:" + Qty);
  clicked_id

  $.ajax({
    url: 'ajaxUpdateInventory/',
    data: {
      'sku': clicked_id,
      'qty': Qty
    },
    success: function (data) {
      $("#idImg").html(data);
    }
  });

  refresh();

}

function callAjaxByURL(theURL)
{
  $.ajax({
    // url: 'ajaxUpdateInventory_Byjson/',
    url: theURL,
    data: {
      'jsonValue': json_object

    },
    success: function (data) {
      $("#idImg").html(data);
    }
  });

}