module.exports = [
  {
    id: 'testextension',
    autoStart: true,
    activate: function (app) {
      console.log(
        'JupyterLab extension testextension is activated!'
      );
      console.log(app.commands);
    }
  }
];
