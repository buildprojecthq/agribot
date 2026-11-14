package com.agrirobot.smartplough

import android.Manifest
import android.annotation.SuppressLint
import android.bluetooth.BluetoothAdapter
import android.bluetooth.BluetoothDevice
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.view.MotionEvent
import android.view.View
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.widget.SwitchCompat
import androidx.core.content.ContextCompat
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

class MainActivity : AppCompatActivity(), BluetoothManager.ConnectionListener {

    private lateinit var bluetoothManager: BluetoothManager

    // UI Elements
    private lateinit var viewStatusDot: View
    private lateinit var tvConnectionStatus: TextView
    private lateinit var tvLastPacket: TextView
    private lateinit var btnConnectToggle: Button

    private lateinit var btnForward: View
    private lateinit var btnBackward: View
    private lateinit var btnLeft: View
    private lateinit var btnRight: View
    private lateinit var btnEmergencyStop: Button

    private lateinit var switchPlough: SwitchCompat
    private lateinit var switchSeed: SwitchCompat
    private lateinit var switchWater: SwitchCompat

    private lateinit var layoutFooter: View
    private lateinit var tvFooterLink: TextView

    private val timeFormat = SimpleDateFormat("HH:mm:ss", Locale.getDefault())

    // Permission Request Launcher
    private val requestPermissionLauncher = registerForActivityResult(
        ActivityResultContracts.RequestMultiplePermissions()
    ) { permissions ->
        val allGranted = permissions.entries.all { it.value }
        if (allGranted) {
            autoConnectToHc05OrPrompt()
        } else {
            Toast.makeText(this, "Bluetooth permissions are required to operate robot.", Toast.LENGTH_LONG).show()
        }
    }

    // Bluetooth Enable Request Launcher
    private val enableBluetoothLauncher = registerForActivityResult(
        ActivityResultContracts.StartActivityForResult()
    ) {
        if (bluetoothManager.isBluetoothEnabled()) {
            autoConnectToHc05OrPrompt()
        } else {
            Toast.makeText(this, "Bluetooth must be enabled to connect to robot.", Toast.LENGTH_SHORT).show()
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        bluetoothManager = BluetoothManager.getInstance()
        bluetoothManager.setConnectionListener(this)

        initViews()
        setupLocomotionTouchListeners()
        setupToolSwitchListeners()
        setupConnectionControls()
        setupFooterLink()

        // Auto-check permissions and auto-connect to HC-05 on app start
        checkPermissionsAndAutoConnect()
    }

    private fun initViews() {
        viewStatusDot = findViewById(R.id.viewStatusDot)
        tvConnectionStatus = findViewById(R.id.tvConnectionStatus)
        tvLastPacket = findViewById(R.id.tvLastPacket)
        btnConnectToggle = findViewById(R.id.btnConnectToggle)

        btnForward = findViewById(R.id.btnForward)
        btnBackward = findViewById(R.id.btnBackward)
        btnLeft = findViewById(R.id.btnLeft)
        btnRight = findViewById(R.id.btnRight)
        btnEmergencyStop = findViewById(R.id.btnEmergencyStop)

        switchPlough = findViewById(R.id.switchPlough)
        switchSeed = findViewById(R.id.switchSeed)
        switchWater = findViewById(R.id.switchWater)

        layoutFooter = findViewById(R.id.layoutFooter)
        tvFooterLink = findViewById(R.id.tvFooterLink)
    }

    private fun setupFooterLink() {
        val openUrlListener = View.OnClickListener { v ->
            v.performHapticFeedback(android.view.HapticFeedbackConstants.VIRTUAL_KEY)
            try {
                val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://buildproject.in/"))
                startActivity(intent)
            } catch (e: Exception) {
                Toast.makeText(this, "Could not open browser: https://buildproject.in/", Toast.LENGTH_SHORT).show()
            }
        }
        layoutFooter.setOnClickListener(openUrlListener)
        tvFooterLink.setOnClickListener(openUrlListener)
    }

    @SuppressLint("ClickableViewAccessibility")
    private fun setupLocomotionTouchListeners() {
        // Touch-and-Hold for Forward
        btnForward.setOnTouchListener { v, event ->
            handleDirectionalTouch(v, event, 'F')
        }

        // Touch-and-Hold for Backward
        btnBackward.setOnTouchListener { v, event ->
            handleDirectionalTouch(v, event, 'B')
        }

        // Touch-and-Hold for Skid Left
        btnLeft.setOnTouchListener { v, event ->
            handleDirectionalTouch(v, event, 'L')
        }

        // Touch-and-Hold for Skid Right
        btnRight.setOnTouchListener { v, event ->
            handleDirectionalTouch(v, event, 'R')
        }

        // Central Emergency STOP button
        btnEmergencyStop.setOnClickListener { v ->
            v.performHapticFeedback(android.view.HapticFeedbackConstants.LONG_PRESS)
            transmitCommand('S')
        }
    }

    private fun handleDirectionalTouch(v: View, event: MotionEvent, commandByte: Char): Boolean {
        when (event.action) {
            MotionEvent.ACTION_DOWN -> {
                v.performHapticFeedback(android.view.HapticFeedbackConstants.VIRTUAL_KEY)
                transmitCommand(commandByte)
                return true
            }
            MotionEvent.ACTION_UP, MotionEvent.ACTION_CANCEL -> {
                v.performHapticFeedback(android.view.HapticFeedbackConstants.VIRTUAL_KEY)
                transmitCommand('S')
                return true
            }
        }
        return false
    }

    private fun setupToolSwitchListeners() {
        // Plough Control: 'P' = Deploy, 'p' = Retract
        switchPlough.setOnCheckedChangeListener { v, isChecked ->
            v.performHapticFeedback(android.view.HapticFeedbackConstants.CLOCK_TICK)
            if (isChecked) {
                transmitCommand('P')
            } else {
                transmitCommand('p')
            }
        }

        // Seed Dispenser: 'D' = Agitate/Dispense, 'd' = Stop/Close
        switchSeed.setOnCheckedChangeListener { v, isChecked ->
            v.performHapticFeedback(android.view.HapticFeedbackConstants.CLOCK_TICK)
            if (isChecked) {
                transmitCommand('D')
            } else {
                transmitCommand('d')
            }
        }

        // Water Pump: 'W' = Pump ON, 'w' = Pump OFF
        switchWater.setOnCheckedChangeListener { v, isChecked ->
            v.performHapticFeedback(android.view.HapticFeedbackConstants.CLOCK_TICK)
            if (isChecked) {
                transmitCommand('W')
            } else {
                transmitCommand('w')
            }
        }
    }

    private fun setupConnectionControls() {
        btnConnectToggle.setOnClickListener {
            if (bluetoothManager.isConnected) {
                bluetoothManager.disconnect()
            } else {
                checkPermissionsAndManualConnect()
            }
        }
    }

    private fun checkPermissionsAndAutoConnect() {
        if (!bluetoothManager.isBluetoothSupported()) {
            Toast.makeText(this, "Bluetooth is not supported on this device.", Toast.LENGTH_SHORT).show()
            return
        }

        val requiredPermissions = getRequiredPermissions()
        if (requiredPermissions.isNotEmpty()) {
            requestPermissionLauncher.launch(requiredPermissions.toTypedArray())
        } else {
            autoConnectToHc05OrPrompt()
        }
    }

    private fun checkPermissionsAndManualConnect() {
        if (!bluetoothManager.isBluetoothSupported()) {
            Toast.makeText(this, "Bluetooth is not supported on this device.", Toast.LENGTH_SHORT).show()
            return
        }

        val requiredPermissions = getRequiredPermissions()
        if (requiredPermissions.isNotEmpty()) {
            requestPermissionLauncher.launch(requiredPermissions.toTypedArray())
        } else {
            if (!bluetoothManager.isBluetoothEnabled()) {
                val enableBtIntent = Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE)
                enableBluetoothLauncher.launch(enableBtIntent)
            } else {
                openDeviceSelectionDialog()
            }
        }
    }

    private fun getRequiredPermissions(): List<String> {
        val permissions = mutableListOf<String>()
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
            if (ContextCompat.checkSelfPermission(this, Manifest.permission.BLUETOOTH_CONNECT) != PackageManager.PERMISSION_GRANTED) {
                permissions.add(Manifest.permission.BLUETOOTH_CONNECT)
            }
            if (ContextCompat.checkSelfPermission(this, Manifest.permission.BLUETOOTH_SCAN) != PackageManager.PERMISSION_GRANTED) {
                permissions.add(Manifest.permission.BLUETOOTH_SCAN)
            }
        } else {
            if (ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
                permissions.add(Manifest.permission.ACCESS_FINE_LOCATION)
            }
        }
        return permissions
    }

    @SuppressLint("MissingPermission")
    private fun autoConnectToHc05OrPrompt() {
        if (!bluetoothManager.isBluetoothEnabled()) {
            val enableBtIntent = Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE)
            enableBluetoothLauncher.launch(enableBtIntent)
            return
        }

        val pairedDevices = bluetoothManager.getPairedDevices()
        val hc05Device = pairedDevices.firstOrNull { device ->
            val name = device.name ?: ""
            name.contains("HC-05", ignoreCase = true) || name.contains("HC-06", ignoreCase = true)
        }

        if (hc05Device != null) {
            Toast.makeText(this, "Auto-connecting to ${hc05Device.name}...", Toast.LENGTH_SHORT).show()
            bluetoothManager.connect(hc05Device)
        } else {
            openDeviceSelectionDialog()
        }
    }

    private fun openDeviceSelectionDialog() {
        val pairedDevices = bluetoothManager.getPairedDevices().toList()
        DeviceListDialog(this, pairedDevices) { selectedDevice ->
            bluetoothManager.connect(selectedDevice)
        }.show()
    }

    private fun transmitCommand(cmd: Char) {
        val timestamp = timeFormat.format(Date())
        if (bluetoothManager.isConnected) {
            bluetoothManager.sendCommand(cmd)
            tvLastPacket.text = "Sent: '$cmd' @ $timestamp"
        } else {
            tvLastPacket.text = "Offline Command: '$cmd' @ $timestamp"
        }
    }

    // ========================================================================
    // Bluetooth Connection Callbacks
    // ========================================================================

    override fun onConnecting() {
        viewStatusDot.setBackgroundResource(R.drawable.bg_dot_connecting)
        tvConnectionStatus.text = getString(R.string.status_connecting)
        btnConnectToggle.isEnabled = false
    }

    override fun onConnected(deviceName: String, deviceAddress: String) {
        viewStatusDot.setBackgroundResource(R.drawable.bg_dot_connected)
        tvConnectionStatus.text = getString(R.string.status_connected, deviceName)
        btnConnectToggle.text = getString(R.string.btn_disconnect)
        btnConnectToggle.setBackgroundResource(R.drawable.bg_pill_btn_danger)
        btnConnectToggle.isEnabled = true
        Toast.makeText(this, "Connected to $deviceName", Toast.LENGTH_SHORT).show()
    }

    override fun onConnectionFailed(error: String) {
        viewStatusDot.setBackgroundResource(R.drawable.bg_dot_disconnected)
        tvConnectionStatus.text = getString(R.string.status_disconnected)
        btnConnectToggle.text = getString(R.string.btn_connect)
        btnConnectToggle.setBackgroundResource(R.drawable.bg_pill_btn)
        btnConnectToggle.isEnabled = true
        Toast.makeText(this, error, Toast.LENGTH_LONG).show()
    }

    override fun onDisconnected() {
        viewStatusDot.setBackgroundResource(R.drawable.bg_dot_disconnected)
        tvConnectionStatus.text = getString(R.string.status_disconnected)
        btnConnectToggle.text = getString(R.string.btn_connect)
        btnConnectToggle.setBackgroundResource(R.drawable.bg_pill_btn)
        btnConnectToggle.isEnabled = true
        Toast.makeText(this, "Bluetooth link disconnected.", Toast.LENGTH_SHORT).show()
    }

    override fun onDataReceived(data: String) {
        tvLastPacket.text = "Rx: ${data.trim()}"
    }

    override fun onDestroy() {
        super.onDestroy()
        if (bluetoothManager.isConnected) {
            bluetoothManager.sendCommand('S')
            bluetoothManager.sendCommand('p')
            bluetoothManager.sendCommand('d')
            bluetoothManager.sendCommand('w')
        }
        bluetoothManager.disconnect()
    }
}
