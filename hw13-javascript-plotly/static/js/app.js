function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel

  // Use `d3.json` to fetch the metadata for a sample
  d3.json(`/metadata/${sample}`).then(function(data) {

    // Use d3 to select the panel with id of `#sample-metadata`
    var panel = d3.select('#sample-metadata');

    // Use `.html("") to clear any existing metadata
    panel.html("")

    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.
    Object.entries(data).forEach(([key, value]) => {

      // add a new line
      var line = panel.append("p");
      line.text(`${key}: ${value}`);

    });

    // BONUS: Build the Gauge Chart
    buildGauge(data.WFREQ);
  })
}

function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  d3.json(`/samples/${sample}`).then(function(data) {
    
    // @TODO: Build a Bubble Chart using the sample data
    var bubbleData = [{
      x: data["otu_ids"],
      y: data["sample_values"],
      text: data["otu_labels"], 
      type: "scatter",
      mode: "markers",
      marker: {
        color: data["otu_ids"],
        // symbol: "circle",
        size: data["sample_values"],
      },
    }];
    var bubbleLayout = {
      title: `<b>Biodiversity of sample ${sample}</b>`,
      xaxis: {
        title: "OTU ID",
        // range: [startDate, endDate],
      },
      yaxis: {
        title: "Value",
        // autorange: true,
        range: [0, Math.max(data["sample_values"])]
        // type: "linear"
      }
    };
    var bubble = document.getElementById("bubble");
    Plotly.newPlot(bubble, bubbleData, bubbleLayout);

    // @TODO: Build a Pie Chart
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
    // Convert data object into array of objects
    var dataArray = [];
    for (var i=0; i<data.otu_ids.length; i++) {
      dataArray.push({
        "sample_values": data.sample_values[i],
        "otu_ids": data.otu_ids[i],
        "otu_labels": data.otu_labels[i]
      })
    }

    // Sort array of objects by sample values
    var dataArraySorted = dataArray.sort((a, b) =>
      parseFloat(b.sample_values) - parseFloat(a.sample_values)
    );

    // Prepare data for plot
    var pieData = [{
      labels: dataArraySorted.map(d => d["otu_ids"]).slice(0,10),
      values: dataArraySorted.map(d => d["sample_values"]).slice(0,10),
      text: dataArraySorted.map(d => d["otu_labels"]).slice(0,10), 
      type: "pie",
      name: dataArraySorted.map(d => d["otu_ids"]).slice(0,10),
      "textinfo": "percent",
    }];
    var pieLayout = {
      title: `<b>Top 10 OTU of sample ${sample}</b>`,
    };
    var pie = document.getElementById("pie");
    Plotly.newPlot(pie, pieData, pieLayout);
  });
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();

