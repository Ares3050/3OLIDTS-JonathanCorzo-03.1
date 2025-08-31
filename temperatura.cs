using System;
using System.Windows.Forms;

namespace ConversorTemperaturas
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Evento Calcular
        private void btnCalcular_Click(object sender, EventArgs e)
        {
            float valor;

            // Celsius a otros
            if (!string.IsNullOrWhiteSpace(txtCelsius.Text) && float.TryParse(txtCelsius.Text, out valor))
            {
                float f = (valor * 9f / 5f) + 32f;
                float k = valor + 273.15f;
                txtFahrenheit.Text = f.ToString("0.00");
                txtKelvin.Text = k.ToString("0.00");
            }
            // Fahrenheit a otros
            else if (!string.IsNullOrWhiteSpace(txtFahrenheit.Text) && float.TryParse(txtFahrenheit.Text, out valor))
            {
                float c = (valor - 32f) * 5f / 9f;
                float k = c + 273.15f;
                txtCelsius.Text = c.ToString("0.00");
                txtKelvin.Text = k.ToString("0.00");
            }
            // Kelvin a otros
            else if (!string.IsNullOrWhiteSpace(txtKelvin.Text) && float.TryParse(txtKelvin.Text, out valor))
            {
                float c = valor - 273.15f;
                float f = (c * 9f / 5f) + 32f;
                txtCelsius.Text = c.ToString("0.00");
                txtFahrenheit.Text = f.ToString("0.00");
            }
            else
            {
                MessageBox.Show("Ingrese un valor numérico válido en al menos una casilla.");
            }
        }

        // Evento Borrar
        private void btnBorrar_Click(object sender, EventArgs e)
        {
            txtCelsius.Clear();
            txtFahrenheit.Clear();
            txtKelvin.Clear();
        }

        // Evento Salir
        private void btnSalir_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
