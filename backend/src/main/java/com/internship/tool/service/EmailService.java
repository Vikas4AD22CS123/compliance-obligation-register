package com.internship.tool.service;

import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.javamail.MimeMessageHelper;
import org.springframework.stereotype.Service;

import jakarta.mail.internet.MimeMessage;

@Service
public class EmailService {

    private final JavaMailSender mailSender;

    public EmailService(JavaMailSender mailSender) {
        this.mailSender = mailSender;
    }

    public void sendComplianceEmail(String to, String title, String messageText) {

        try {
            MimeMessage message = mailSender.createMimeMessage();
            MimeMessageHelper helper = new MimeMessageHelper(message, true);

            helper.setTo(to);
            helper.setSubject("Compliance Notification");
            helper.setText(
                "<h2>Compliance Alert</h2>" +
                "<p><b>Title:</b> " + title + "</p>" +
                "<p><b>Message:</b> " + messageText + "</p>",
                true
            );

            mailSender.send(message);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}