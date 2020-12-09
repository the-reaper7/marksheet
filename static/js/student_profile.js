let key = document.getElementById("serial_number").innerText;
let semesterChart = document.getElementById("semesterChart");
let marksChart = document.getElementById("marksChart");
let marksheet = document.getElementById("marksheet");
$.ajax({
  url: "get-marks/" + key,
  type: "GET",
  dataType: "json",
  success: function (data) {
    average = data[0]["average"];
    marks = data[0];

    var ctx = semesterChart.getContext("2d");
    var mtx = marksChart.getContext("2d");

    // average chart
    new Chart(ctx, {
      type: "bar",
      data: {
        labels: ["Sem 1", "Sem 2", "Sem 3", "Sem 4"],
        datasets: [
          {
            label: "Average",
            backgroundColor: ["#007BFF", "#FFEB3B", "#F44336", "#FB8C00"],
            data: [
              average["semester 1"],
              average["semester 2"],
              average["semester 3"],
              average["semester 4"],
            ],
          },
        ],
      },
      options: {
        responsive: true,
        legend: {
          position: "top",
          display: false,
        },
        title: {
          display: true,
          text: "Semester Bar Chart",
        },
      },
    });
    // marks chart
    new Chart(mtx, {
      type: "line",
      data: {
        labels: ["Maths", "Science", "CS", "Hindi"],
        datasets: [
          {
            label: "Semester 1",
            backgroundColor: "#007BFF",
            borderColor: "#007BFF",
            data: marks["semester 1"],
            fill: false,
          },
          {
            label: "Semester 2",
            backgroundColor: "#FFEB3B",
            borderColor: "#FFEB3B",
            data: marks["semester 2"],
            fill: false,
          },
          {
            label: "Semester 3",
            backgroundColor: "#F44336",
            borderColor: "#F44336",
            data: marks["semester 3"],
            fill: false,
          },
          {
            label: "Semester 4",
            backgroundColor: "#FB8C00",
            borderColor: "#FB8C00",
            data: marks["semester 4"],
            fill: false,
          },
        ],
      },
      options: {
        responsive: true,
        legend: {
          position: "top",
          display: false,
        },
        title: {
          display: true,
          text: "Marks Bar Chart",
        },
      },
    });
    let mark = [
      marks["semester 1"],
      marks["semester 2"],
      marks["semester 3"],
      marks["semester 4"],
    ];
    let id = "semester-marksheet-";
    let addMarksheet = function (data) {
      for (var x = 0; x <= 3; x++) {
        let divMarksheet = document.createElement("div");
        divMarksheet.className = "col-sm-6 mb-3";
        divMarksheet.id = id + (x + 1);

        let divMarksheetCard = document.createElement("div");
        divMarksheetCard.className = "card h-100";
        divMarksheetCard.id = "marksheet-card";

        let divMarksheetCardBody = document.createElement("div");
        divMarksheetCardBody.className = "card-body";
        divMarksheetCardBody.id = "marksheet-card-body";

        let title = document.createElement("h6");
        title.className = "d-flex align-items-center mb-3";
        title.innerText = "Marksheet Semester " + (x + 1);

        divMarksheetCardBody.appendChild(title);

        let subjects = [
          "Maths",
          "Science",
          "Computer Science",
          "English",
          "Hindi",
        ];
        for (var z = 0; z <= 4; z++) {
          let small = document.createElement("small");
          let mark_subject = data[x][z];
          small.innerText = subjects[z] + " : " + mark_subject;

          let progress = document.createElement("div");
          progress.className = "progress mb-3";
          progress.style.height = "5px";

          let progressBar = document.createElement("div");
          progressBar.className = "progress-bar bg-primary";
          progressBar.role = "progressbar";
          progressBar.style.width = mark_subject + "%";
          progressBar.style.ariaValuenow = mark_subject;
          progressBar.setAttribute("aria-valuenow", mark_subject);
          progressBar.setAttribute("aria-valuemin", 0);
          progressBar.setAttribute("aria-valuemax", 100);

          progress.appendChild(progressBar);
          divMarksheetCardBody.appendChild(small);
          divMarksheetCardBody.append(progress);
        }

        divMarksheetCard.appendChild(divMarksheetCardBody);
        divMarksheet.appendChild(divMarksheetCard);
        marksheet.appendChild(divMarksheet);
      }
    };
    addMarksheet(mark);
  },
});
