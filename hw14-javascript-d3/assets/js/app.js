// D3 Scatterplot Assignment

// Students:
// =========
// Follow your written instructions and create a scatter plot with D3.js.

// When the browser window is resized, makeResponsive() is called.
d3.select(window).on("resize", makeResponsive);

// When the browser loads, loadChart() is called
loadChart();

// Define responsive function
function makeResponsive() {

  // if the SVG area isn't empty when the browser loads, remove it and replace it with a resized version of the chart
  var svgArea = d3.select("body").select("svg");

  if (!svgArea.empty()) {
    svgArea.remove();
    loadChart();
  }
}

// Define the chart rendering function
function loadChart() {
  var svgHeight = window.innerHeight;
  var svgWidth = window.innerWidth;

  var margin = {
    top: 20,
    right: 40,
    bottom: 100,
    left: 100
  };

  var width = svgWidth - margin.left - margin.right;
  var height = svgHeight - margin.top - margin.bottom;

  // Create an SVG wrapper, append an SVG group that will hold our chart,
  // and shift the latter by left and top margins.
  var svg = d3
    .select("body")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

  // Append an SVG group
  var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

  // Initial Params
  var chosenXAxis = "poverty";
  var chosenYAxis = "healthcare";

  // Retrieve data from the CSV file and execute everything below
  d3.csv("data/data.csv", function(err, healthData) {
    if (err) throw err;

    // parse data
    healthData.forEach(function(data) {
      data.poverty = +data.poverty;
      data.age = +data.age;
      data.income = +data.income;
      data.healthcare = +data.healthcare;
      data.obesity = +data.obesity;
      data.smokes = +data.smokes;
    });

    // console.log(healthData);

    // xLinearScale function above csv import
    var xLinearScale = xScale(healthData, chosenXAxis);
    
    // yLinearScale function above csv import
    var yLinearScale = yScale(healthData, chosenYAxis);

    // Create initial axis functions
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    // Responsive axis tick spacing
    if (svgWidth < 500) {
      var leftAxis = d3.axisLeft(yLinearScale).ticks(5);
    }
    else {
      var leftAxis = d3.axisLeft(yLinearScale).ticks(10);
    }

    // append x axis
    var xAxis = chartGroup.append("g")
      .classed("x-axis", true)
      .attr("transform", `translate(0, ${height})`)
      .call(bottomAxis);

    // append y axis
    var yAxis = chartGroup.append("g")
      .classed("y-axis", true)
      .call(leftAxis);

    // append initial circles
    var circlesGroup = chartGroup.append("g")
      .selectAll("circle")
      .data(healthData)
      .enter()
      .append("circle")
      .attr("cx", d => xLinearScale(d[chosenXAxis]))
      .attr("cy", d => yLinearScale(d[chosenYAxis]))
      .attr("r", 12)
      .attr("fill", "lightblue")
      .attr("opacity", ".8");

    // append text labels
    var textsGroup = chartGroup.append("g")
      .selectAll("text")
      .data(healthData)
      .enter()
      .append("text")
      .classed("text-group", true)
      .text(d => d.abbr)
      .attr("x", d => xLinearScale(d[chosenXAxis]))
      .attr("y", d => yLinearScale(d[chosenYAxis]))
      .attr("text-anchor", "middle")
      .attr("alignment-baseline", "central")
      .attr("font_family", "sans-serif")  // Font type
      .attr("font-size", "11px")  // Font size
      .attr("fill", "white")   // Font color
      .style("font-weight", "bold");

    console.log(circlesGroup);
    console.log(textsGroup);

    // Responsive scatter size and text labels
    if (svgWidth < 500) {
      circlesGroup.attr("r", 5);
      textsGroup.style("display", "none");
    }
    else {
      circlesGroup.attr("r", 12);
      textsGroup.style("display", "inline");
    }

    // Create group for  3 x-axis labels
    var labelsGroup = chartGroup.append("g")
      .attr("transform", `translate(${width / 2}, ${height + 20})`)
      .classed("xLabel", true);

    var povertyLabel = labelsGroup.append("text")
      .attr("x", 0)
      .attr("y", 20)
      .attr("value", "poverty") // value to grab for event listener
      .classed("active", true)
      .text("In Poverty (%)");

    var ageLabel = labelsGroup.append("text")
      .attr("x", 0)
      .attr("y", 40)
      .attr("value", "age") // value to grab for event listener
      .classed("inactive", true)
      .text("Age (Median)");

    var incomeLabel = labelsGroup.append("text")
      .attr("x", 0)
      .attr("y", 60)
      .attr("value", "income") // value to grab for event listener
      .classed("inactive", true)
      .text("Household Income (Median)");
    
    // Create group for  3 y-axis labels
    var ylabelsGroup = chartGroup.append("g")
      .attr("transform", "rotate(-90)")
      .classed("yLabel", true);

    var healthcareLabel = ylabelsGroup.append("text")
      .attr("y", 0 - 50)
      .attr("x", 0 - (height / 2))
      .attr("value", "healthcare")
      .attr("dy", "1em")
      // .classed("axis-text", true)
      .classed("active", true)
      .text("Lacks Healthcare (%)");

    var obesityLabel = ylabelsGroup.append("text")
      .attr("y", 0 - 70)
      .attr("x", 0 - (height / 2))
      .attr("value", "obesity")
      .attr("dy", "1em")
      // .classed("axis-text", true)
      .classed("inactive", true)
      .text("Obese (%)");

    var smokesLabel = ylabelsGroup.append("text")
      .attr("y", 0 - 90)
      .attr("x", 0 - (height / 2))
      .attr("value", "smokes")
      .attr("dy", "1em")
      // .classed("axis-text", true)
      .classed("inactive", true)
      .text("Smokes (%)");

    // updateToolTip function above csv import
    var circlesGroup = updateToolTip(chosenXAxis, circlesGroup);
    circlesGroup = updateYToolTip(chosenYAxis, circlesGroup);

    // x axis labels event listener
    labelsGroup.selectAll("text")
      .on("click", function() {
        // get value of selection
        var value = d3.select(this).attr("value");
        if (value !== chosenXAxis) {

          // replaces chosenXaxis with value
          chosenXAxis = value;

          // console.log(chosenXAxis)

          // functions here found above csv import
          // updates x scale for new data
          xLinearScale = xScale(healthData, chosenXAxis);

          // updates x axis with transition
          xAxis = renderAxes(xLinearScale, xAxis);

          // updates circles with new x values
          circlesGroup = renderCircles(circlesGroup, xLinearScale, chosenXAxis);

          // update texts with new x values
          textsGroup = renderTexts(textsGroup, xLinearScale, chosenXAxis);

          // updates tooltips with new info
          circlesGroup = updateToolTip(chosenXAxis, circlesGroup);

          // changes classes to change bold text
          if (chosenXAxis === "age") {
            ageLabel
              .classed("active", true)
              .classed("inactive", false);
            povertyLabel
              .classed("active", false)
              .classed("inactive", true);
            incomeLabel
              .classed("active", false)
              .classed("inactive", true);
          }
          else if (chosenXAxis === "poverty") {
            ageLabel
              .classed("active", false)
              .classed("inactive", true);
            povertyLabel
              .classed("active", true)
              .classed("inactive", false);
            incomeLabel
              .classed("active", false)
              .classed("inactive", true);
          }
          else if (chosenXAxis === "income") {
            ageLabel
              .classed("active", false)
              .classed("inactive", true);
            povertyLabel
              .classed("active", false)
              .classed("inactive", true);
            incomeLabel
              .classed("active", true)
              .classed("inactive", false);
          }
        }
      });

    // y axis labels event listener
    ylabelsGroup.selectAll("text")
      .on("click", function() {
        // get value of selection
        var value = d3.select(this).attr("value");
        if (value !== chosenYAxis) {

          // replaces chosenXaxis with value
          chosenYAxis = value;

          // console.log(chosenYAxis)

          // functions here found above csv import
          // updates x scale for new data
          yLinearScale = yScale(healthData, chosenYAxis);

          // updates x axis with transition
          yAxis = renderYAxes(yLinearScale, yAxis);

          // updates circles with new y values
          circlesGroup = renderYCircles(circlesGroup, yLinearScale, chosenYAxis);

          // update texts with new y values
          textsGroup = renderYTexts(textsGroup, yLinearScale, chosenYAxis);

          // updates tooltips with new info
          circlesGroup = updateYToolTip(chosenYAxis, circlesGroup);

          // changes classes to change bold text
          if (chosenYAxis === "healthcare") {
            healthcareLabel
              .classed("active", true)
              .classed("inactive", false);
            obesityLabel
              .classed("active", false)
              .classed("inactive", true);
            smokesLabel
              .classed("active", false)
              .classed("inactive", true);
          }
          else if (chosenYAxis === "obesity") {
            healthcareLabel
              .classed("active", false)
              .classed("inactive", true);
            obesityLabel
              .classed("active", true)
              .classed("inactive", false);
            smokesLabel
              .classed("active", false)
              .classed("inactive", true);
          }
          else if (chosenYAxis === "smokes") {
            healthcareLabel
              .classed("active", false)
              .classed("inactive", true);
            obesityLabel
              .classed("active", false)
              .classed("inactive", true);
            smokesLabel
              .classed("active", true)
              .classed("inactive", false);
          }
        }
      });
  });

  /**==================================== */
  // function used for updating x-scale var upon click on axis label
  function xScale(healthData, chosenXAxis) {
    // create scales
    var xLinearScale = d3.scaleLinear()
      .domain([d3.min(healthData, d => d[chosenXAxis]) * 0.8,
        d3.max(healthData, d => d[chosenXAxis]) * 1.2
      ])
      .range([0, width]);

    return xLinearScale;
  }

  // function used for updating x-scale var upon click on axis label
  function yScale(healthData, chosenYAxis) {
    // create scales
    var yLinearScale = d3.scaleLinear()
      .domain([0, d3.max(healthData, d => d[chosenYAxis]) * 1.2])
      .range([height, 0]);

    return yLinearScale;
  }

  // function used for updating xAxis var upon click on axis label
  function renderAxes(newXScale, xAxis) {
    var bottomAxis = d3.axisBottom(newXScale);

    xAxis.transition()
      .duration(1000)
      .call(bottomAxis);

    return xAxis;
  }

  // function used for updating xAxis var upon click on axis label
  function renderYAxes(newYScale, yAxis) {
    var leftAxis = d3.axisLeft(newYScale);

    yAxis.transition()
      .duration(1000)
      .call(leftAxis);

    return yAxis;
  }

  // function used for updating circles group with a transition to
  // new circles
  function renderCircles(circlesGroup, newXScale, chosenXAxis) {

    circlesGroup.transition()
      .duration(1000)
      .attr("cx", d => newXScale(d[chosenXAxis]));

    return circlesGroup;
  }

  function renderYCircles(circlesGroup, newYScale, chosenYAxis) {

    circlesGroup.transition()
      .duration(1000)
      .attr("cy", d => newYScale(d[chosenYAxis]));

    return circlesGroup;
  }

  // function used for updating texts group with a transition to
  // new circles
  function renderTexts(textsGroup, newXScale, chosenXAxis) {

    textsGroup.transition()
      .duration(1000)
      .attr("x", d => newXScale(d[chosenXAxis]));

    return textsGroup;
  }

  function renderYTexts(textsGroup, newYScale, chosenYAxis) {

    textsGroup.transition()
      .duration(1000)
      .attr("y", d => newYScale(d[chosenYAxis]));

    return textsGroup;
  }

  // function used for updating circles group with new tooltip
  function updateToolTip(chosenXAxis, circlesGroup) {

    if (chosenXAxis === "poverty") {
      var label = "Poverty (%):";
    }
    else if (chosenXAxis === "age") {
      var label = "Age: ";
    }
    else if (chosenXAxis === "income") {
      var label = "Household Income:";
    }

    var chosenYAxis = d3.select(".yLabel").select(".active").attr("value");

    if (chosenYAxis === "healthcare") {
      var yLabel = "Lacks Healthcare (%):";
    }
    else if (chosenYAxis === "obesity") {
      var yLabel = "Obesity (%):";
    }
    else if (chosenYAxis === "smokes") {
      var yLabel = "Smokes (%):";
    }

    var toolTip = d3.tip()
      .attr("class", "tooltip")
      .offset([80, -60])
      .html(function(d) {
        return (`${d.abbr}<br>${label} ${d[chosenXAxis]}<br>${yLabel} ${d[chosenYAxis]}`);
      });

    circlesGroup.call(toolTip);

    circlesGroup.on("mouseover", toolTip.show)
      .on("mouseout", toolTip.hide);

    return circlesGroup;
  }

  // function used for updating circles group with new tooltip
  function updateYToolTip(chosenYAxis, circlesGroup) {

    if (chosenYAxis === "healthcare") {
      var yLabel = "Lacks Healthcare (%):";
    }
    else if (chosenYAxis === "obesity") {
      var yLabel = "Obesity (%):";
    }
    else if (chosenYAxis === "smokes") {
      var yLabel = "Smokes (%):";
    }

    var chosenXAxis = d3.select(".xLabel").select(".active").attr("value");

    if (chosenXAxis === "poverty") {
      var label = "Poverty (%):";
    }
    else if (chosenXAxis === "age") {
      var label = "Age: ";
    }
    else if (chosenXAxis === "income") {
      var label = "Household Income:";
    }

    var toolTip = d3.tip()
      .attr("class", "tooltip")
      .offset([80, -60])
      .html(function(d) {
        return (`${d.abbr}<br>${label} ${d[chosenXAxis]}<br>${yLabel} ${d[chosenYAxis]}`);
      });

    circlesGroup.call(toolTip);

    circlesGroup.on("mouseover", toolTip.show)
      .on("mouseout", toolTip.hide);

    return circlesGroup;
  }

}